# from django.conf.global_settings import LANGUAGES
import operator
from functools import reduce

from django.db.models import Q
from polymorphic.managers import PolymorphicManager, PolymorphicQuerySet
from treebeard.mp_tree import MP_NodeQuerySet, get_result_class


class PolmymorphicTreeQuerySet(MP_NodeQuerySet, PolymorphicQuerySet):
    # this is 99% copy/paste from MP_NodeQuerySet
    # we only make sure that the final queryset is non-polymorphic
    def delete(self, *args, **kwargs):
        """
        Custom delete method, will remove all descendant nodes to ensure a
        consistent tree (no orphans)

        :returns: tuple of the number of objects deleted and a dictionary
                  with the number of deletions per object type
        """
        # we'll have to manually run through all the nodes that are going
        # to be deleted and remove nodes from the list if an ancestor is
        # already getting removed, since that would be redundant
        removed = {}
        for node in self.order_by("depth", "path"):
            found = False
            for depth in range(1, int(len(node.path) / node.steplen)):
                path = node._get_basepath(node.path, depth)
                if path in removed:
                    # we are already removing a parent of this node
                    # skip
                    found = True
                    break
            if not found:
                removed[node.path] = node

        # ok, got the minimal list of nodes to remove...
        # we must also remove their children
        # and update every parent node's numchild attribute
        # LOTS OF FUN HERE!
        parents = {}
        toremove = []
        for path, node in removed.items():
            parentpath = node._get_basepath(node.path, node.depth - 1)
            if parentpath:
                if parentpath not in parents:
                    parents[parentpath] = node.get_parent(True)
                parent = parents[parentpath]
                if parent and parent.numchild > 0:
                    parent.numchild -= 1
                    parent.save()
            if node.is_leaf():
                toremove.append(Q(path=node.path))
            else:
                toremove.append(Q(path__startswith=node.path))

        # Django will handle this as a SELECT and then a DELETE of
        # ids, and will deal with removing related objects
        model = get_result_class(self.model)
        if toremove:
            # qset = model.objects.filter(reduce(operator.or_, toremove))
            # changed below to be non-polymorphic, otherwise this fails
            qset = model.objects.non_polymorphic().filter(reduce(operator.or_, toremove))
        else:
            qset = model.objects.none()
        return super(MP_NodeQuerySet, qset).delete(*args, **kwargs)

    delete.alters_data = True
    delete.queryset_only = True


class PolymorphicTreeManager(PolymorphicManager):
    queryset_class = PolmymorphicTreeQuerySet

    def get_queryset(self):
        return super().get_queryset().order_by("path")
