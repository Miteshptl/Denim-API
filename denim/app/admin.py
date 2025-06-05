from django.contrib import admin
from .models import Product, ProductImage

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  

class ProductAdmin(admin.ModelAdmin):
    list_display=[
        "name",
        "category",
        "description",
        "price",
        "stock"
        ]
    inlines = [ProductImageInline]

admin.site.register(Product,ProductAdmin)