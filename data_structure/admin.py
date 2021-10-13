from django.contrib import admin

from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


from .models import IikoGroup, IikoDish, Item


@admin.register(Item)
class ItemAdmin(TreeAdmin):
    # list_display = ('title', 'entity_type', 'is_edited', 'timestamp', '_position', '_ref_node_id',)
    form = movenodeform_factory(Item)


@admin.register(IikoGroup)
class GroupAdmin(admin.ModelAdmin):

    pass


@admin.register(IikoDish)
class DishAdmin(admin.ModelAdmin):
    pass

# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#
#     pass