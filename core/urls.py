from rest_framework.routers import DefaultRouter
from core.views import ProductViewSet
from django.urls import path, include

router = DefaultRouter()
router.register("products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
