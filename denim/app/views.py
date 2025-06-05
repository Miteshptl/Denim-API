from django.shortcuts import render
from .models import Product, ProductImage
from rest_framework import generics
from .serializers import ProductSerializer, ProductImageSerializer



# Create your views here.

# @app_view([["GET"]])
# def Apioverview(req):
#     api_urls = {
#         "AllProducts": "/",
#         "AddProducts": "/add/",
#     }

class AllProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class AddProducts(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer