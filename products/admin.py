from django.contrib import admin
from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'slug', 'description')
    list_display_links = ('__unicode__', 'slug')
    prepopulated_fields = {'slug': ['name']}  # look here - intresting thing
    class Meta:
        model = Products

admin.site.register(Products, ProductsAdmin)
