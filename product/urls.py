from django.urls import include, path
from rest_framework import routers

from .viewsets import BrandViewSet, CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register("category", CategoryViewSet, basename="category")
router.register("brand", BrandViewSet, basename="brand")
router.register("product", ProductViewSet, basename="product")

urlpatterns = [path("", include(router.urls))]
