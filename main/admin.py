from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'breed', 'time_create', 'price', 'image_show')
    list_display_links = ('id', 'breed')
    search_fields = ('breed', 'content')
    prepopulated_fields = {"slug": ("breed",)}

    def image_show(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width='60' />".format(obj.photo.url))
        else:
            default_image_url = '<path/to/default/image.jpg>'
            return mark_safe("<img src='{}' width='60' />".format(default_image_url))


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Pet, PetAdmin)
admin.site.register(Category, CategoryAdmin)
