from django.contrib import admin

from polymorphic_treebeard.admin import PolymorphicTreeAdmin, PolymorphicTreeChildAdmin

from .models import BaseSample, Child, RelatedModel, SampleTypeA, SampleTypeB

admin.site.register(RelatedModel)
admin.site.register(Child)


class ChildInline(admin.TabularInline):
    model = Child
    extra = 1


@admin.register(BaseSample)
class BaseSampleAdmin(PolymorphicTreeAdmin):
    base_model = BaseSample
    child_models = [SampleTypeA, SampleTypeB]


@admin.register(SampleTypeA)
class SampleTypeA(PolymorphicTreeChildAdmin):
    inlines = [ChildInline]

    base_model = BaseSample


@admin.register(SampleTypeB)
class SampleTypeB(PolymorphicTreeChildAdmin):
    base_model = BaseSample
