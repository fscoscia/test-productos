from django.contrib import admin

from core.models import Product, Category, ProductImage


class ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "state"]
    list_display_links = ["id", "name", "state"]
    inlines = [ImageInline]


admin.site.register(Category)
