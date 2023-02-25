from django.contrib import admin

from .models import *


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'breed', 'time_create')
    list_display_links = ('id', 'breed')
    search_fields = ('breed', 'content')
    prepopulated_fields = {"slug": ("breed",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Pet, PetAdmin)
admin.site.register(Category, CategoryAdmin)
