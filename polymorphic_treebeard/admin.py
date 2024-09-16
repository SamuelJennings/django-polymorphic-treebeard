from polymorphic.admin import PolymorphicChildModelAdmin, PolymorphicParentModelAdmin
from treebeard.admin import TreeAdmin

from .forms import movepolynodeform_factory


class PolymorphicTreeAdmin(PolymorphicParentModelAdmin, TreeAdmin):
    pass


class PolymorphicTreeChildAdmin(TreeAdmin, PolymorphicChildModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        self.base_form = movepolynodeform_factory(self.model)
        return super().get_form(request, obj, **kwargs)

    def delete_view(self, request, object_id, context=None):
        return super().delete_view(request, object_id, context)

    def get_subclass_fields(self, request, obj=None):
        subclass_fields = super().get_subclass_fields(request, obj)
        always_exclude = ["path", "depth", "numchild"]
        return [f for f in subclass_fields if f not in always_exclude]
