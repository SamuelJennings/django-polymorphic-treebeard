import uuid

from django.db import models

from polymorphic_treebeard.models import PolymorphicMP_Node


class RelatedModel(models.Model):
    name = models.CharField("name", max_length=200, help_text="Enter a string of up to 200 characters.")

    class Meta:
        verbose_name = "Related Model"
        verbose_name_plural = "Related Models"

    def __str__(self):
        return self.name


class BaseSample(PolymorphicMP_Node):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="ID",
        primary_key=True,
    )

    name = models.CharField("name", max_length=200, help_text="Enter a string of up to 200 characters.")

    related_field = models.ForeignKey(RelatedModel, on_delete=models.CASCADE, null=True, blank=True)


class Child(models.Model):
    name = models.CharField("name", max_length=200, help_text="Enter a string of up to 200 characters.")
    parent = models.ForeignKey(BaseSample, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Child"
        verbose_name_plural = "Children"

    def __str__(self):
        return self.name


class SampleTypeA(BaseSample):
    a_field = models.CharField("a_field", max_length=200, help_text="Enter a string of up to 200 characters.")
    testr = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Sample Type A"
        verbose_name_plural = "Sample Types A"


class SampleTypeB(BaseSample):
    # ALLOWED_PARENTS = [SampleTypeA, "self", "example.BaseSample"]

    b_field = models.CharField("b_field", max_length=200, help_text="Enter a string of up to 200 characters.")

    class Meta:
        verbose_name = "Sample Type B"
        verbose_name_plural = "Sample Types B"

    @classmethod
    def get_allowed_parents(cls):
        return cls.ALLOWED_PARENTS
