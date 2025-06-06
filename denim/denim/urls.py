"""
URL configuration for denim project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app.views import AllProducts, AddProducts, UpdateProducts, DeleteProducts, BannerView, BannerAdd, Bannerdelete
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Apioverview, name='Apioverview'),
    path("all/", AllProducts.as_view(), name='AllProducts'),
    path("add/", AddProducts.as_view(), name='AddProducts'),
    path("product/update/<int:pk>/", views.UpdateProducts.as_view(), name='UpdateProducts'),
    path("product/<int:pk>/delete/", views.DeleteProducts.as_view(), name='DeleteProducts'),
    path("banner/", BannerView.as_view(), name='BannerView'),
    path("banner/add/", views.BannerAdd.as_view(), name='BannerAdd'),
    path("banner/view/", views.BannerView.as_view(), name='BannerView'),
    path("banner/delete/<int:pk>/", views.Bannerdelete.as_view(), name='BannerDelete'),
]
