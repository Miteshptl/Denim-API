from django.shortcuts import render
from .models import Product, ProductImage, Banner
from rest_framework import generics
from .serializers import ProductSerializer, ProductImageSerializer, BannerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def Apioverview(req):
    api_urls = {
        "AllProducts": "/all/",
        "AddProducts": "/add/",
        "UpdateProducts": "/product/update/pk/",
        "DeleteProducts": "/product/pk/delete/",
        "Banner": "/banner/",
        "BannerView": "/banner/view/",
        "BannerAdd": "/banner/add/",
        "BannerDelete": "/banner/delete/pk/",

    }
    return Response(api_urls)

class AllProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class AddProducts(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    
class UpdateProducts(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = 'pk'


class DeleteProducts(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BannerView(APIView):
    def get(self, request):
        banners = Banner.objects.all()
        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BannerAdd(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = BannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BannerView(APIView):
    def get(self, request):
        banners = Banner.objects.all()
        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Bannerdelete(APIView):
    def delete(self, request, pk):
        try:
            banner = Banner.objects.get(pk=pk)
            banner.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Banner.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

