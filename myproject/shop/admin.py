from django.contrib import admin
from .models import Product, Category, Visitor


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'stock',
        'created_at',
    )

    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = (
        'ip_address',
        'first_seen',
        'last_seen',
        'visits',
    )

    search_fields = ('ip_address',)

    readonly_fields = (
        'ip_address',
        'first_seen',
        'last_seen',
        'visits',
    )