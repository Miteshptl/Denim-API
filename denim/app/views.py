from django.shortcuts import render
from .models import Product, ProductImage
from rest_framework import viewsets
from .serializers import ProductSerializer, ProductImageSerializer



# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer