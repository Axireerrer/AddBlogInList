from django.contrib import admin
from django.utils.safestring import mark_safe

from WebSite.models import FamousPerson


@admin.register(FamousPerson)
class AdminForm(admin.ModelAdmin):
    list_display = ['name', 'surname', 'age', 'slug', 'category', 'description', 'image']
    list_filter = ['slug']
    list_display_links = ['name', 'surname', 'age', 'description', 'slug', 'category', 'image']
    list_per_page = 2
    search_fields = ['name']

