from polymorphic.models import PolymorphicModel
from treebeard.mp_tree import MP_Node, get_result_class

from .managers import PolymorphicTreeManager
from .utils import resolve_model_reference


class PolymorphicMP_Node(MP_Node, PolymorphicModel):
    ALLOWED_PARENTS = []
    ALLOWED_CHILDREN = []

    objects = PolymorphicTreeManager()

    class Meta:
        abstract = True

    @classmethod
    def get_root_nodes(cls):
        """Override the default get_root_nodes method to return only the root nodes of the current class."""
        results = get_result_class(cls).objects.filter(depth=1).order_by("path")
        if cls.ALLOWED_PARENTS:
            return results.instance_of(*cls.get_allowed_parents())
        return results

    @classmethod
    def get_allowed_children(cls):
        if cls.ALLOWED_CHILDREN:
            return cls.ALLOWED_CHILDREN
        return [resolve_model_reference(parent, cls) for parent in cls.ALLOWED_CHILDREN]

    @classmethod
    def get_allowed_parents(cls):
        if cls.ALLOWED_PARENTS:
            return cls.ALLOWED_PARENTS
        return [resolve_model_reference(parent, cls) for parent in cls.ALLOWED_PARENTS]
