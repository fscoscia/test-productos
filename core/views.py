from django.shortcuts import render
from rest_framework import viewsets, mixins

from core.models import Product
from core.serializers import (
    ProductDetailSerializer,
    ProductListSerializer,
    ProductPartialSerializer,
)


class ProductViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Product.objects.all()
    serializer_class = ProductPartialSerializer
    search_fields = [
        "name",
    ]
    filterset_fields = ["state", "categories"]

    def get_serializer_class(self):
        if self.request.user.is_anonymous:
            return self.serializer_class
        if self.action in ["retrieve", "update"]:
            return ProductDetailSerializer
        return ProductListSerializer
