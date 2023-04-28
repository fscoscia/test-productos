from rest_framework.routers import DefaultRouter
from core.views import CategoryViewSet, ProductViewSet
from django.urls import path, include

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
