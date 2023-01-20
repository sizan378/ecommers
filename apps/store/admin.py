from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_by', 'author', 'slug', 'price', 'is_active','is_stock']
    list_filter = ['is_stock', 'is_active']
    list_editable = ['price', 'is_stock', 'is_active']
    prepopulated_fields = {'slug':('title',),}

admin.site.register(Product, ProductAdmin)