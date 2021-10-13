from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from treebeard.mp_tree import MP_Node


class BaseEntity(models.Model):

    title = models.CharField(max_length=120)

    class Meta:
        abstract = True


class IikoGroup(BaseEntity):

    pass


class IikoDish(BaseEntity):

    pass


class Item(MP_Node, BaseEntity):

    def __str__(self):
        return f'{self.entity_type.title}: {self.title}'

    entity_choices = models.Q(model='iikogroup') | models.Q(model='iikodish')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=entity_choices)
    object_id = models.PositiveIntegerField()
    entity_type = GenericForeignKey('content_type', 'object_id')
