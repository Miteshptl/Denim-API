from rest_framework import serializers
from .models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source='image', read_only=True)

    class Meta:
        model = ProductImage
        fields = ['id', 'image_url']

class ProductSerializer(serializers.ModelSerializer):
    # write-only for upload
    images_upload = ProductImageSerializer(many=True, write_only=True, source='images')
    # read-only for display
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description', 'price', 'stock', 'images_upload', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        product = Product.objects.create(**validated_data)
        for image_data in images_data:
            ProductImage.objects.create(Product=product, **image_data)
        return product

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage  # Assuming Banner is similar to ProductImage
        fields = ['id', 'image']  # Adjust fields as necessary
        read_only_fields = ['id']  # Assuming ID is auto-generated