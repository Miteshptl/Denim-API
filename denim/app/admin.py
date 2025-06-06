from django.contrib import admin
from .models import Product, ProductImage, Banner

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

class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
    search_fields = ['id']

admin.site.register(Product,ProductAdmin)
admin.site.register(Banner,BannerAdmin)