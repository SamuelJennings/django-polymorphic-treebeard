from django.forms import ModelForm
from polymorphic.utils import get_base_polymorphic_model
from treebeard.forms import MoveNodeForm, movenodeform_factory


class PolymorphicTreeForm(MoveNodeForm):
    def save(self, commit=True):
        position_type, reference_node_id = self._clean_cleaned_data()
        base_model = get_base_polymorphic_model(self._meta.model)
        if self.instance._state.adding:
            if reference_node_id:
                reference_node = base_model.objects.get(pk=reference_node_id)
                self.instance = reference_node.add_child(instance=self.instance)
                self.instance.move(reference_node, pos=position_type)
            else:
                self.instance = base_model.add_root(instance=self.instance)
        else:
            self.instance.save()
            if reference_node_id:
                reference_node = base_model.objects.get(pk=reference_node_id)
                self.instance.move(reference_node, pos=position_type)
            else:
                if self.is_sorted:
                    pos = "sorted-sibling"
                else:
                    pos = "first-sibling"
                self.instance.move(base_model.get_first_root_node(), pos)
        # Reload the instance
        self.instance.refresh_from_db()
        # skip the MoveNodeForm.save() method
        ModelForm.save(self, commit=commit)
        return self.instance

    # @classmethod
    # def add_subtree(cls, for_node, node, options):
    #     """Recursively build options tree."""
    #     if cls.is_loop_safe(for_node, node):
    #         for item, _ in node.get_annotated_list(node):
    #             options.append((item.pk, mark_safe(cls.mk_indent(item.get_depth()) + escape(item))))

    # @classmethod
    # def mk_dropdown_tree(cls, model, for_node=None):
    #     """Creates a tree-like list of choices"""

    #     options = [(None, _("-- root --"))]
    #     root_nodes = model.get_root_nodes().instance_of(*model.get_allowed_children())
    #     for node in root_nodes:
    #         if cls.is_loop_safe(for_node, node):
    #             pass
    #             for item, c in node.get_annotated_list(node).instance_of(*model.get_allowed_children()):
    #                 options.append((item.pk, mark_safe(cls.mk_indent(item.get_depth()) + escape(item))))
    #     return options


def movepolynodeform_factory(
    model,
    form=PolymorphicTreeForm,
    fields=None,
    exclude=None,
    formfield_callback=None,
    widgets=None,
):
    """Wrapper around movenodeform_factory that uses PolymorphicTreeForm."""
    return movenodeform_factory(model, form, fields, exclude, formfield_callback, widgets)
