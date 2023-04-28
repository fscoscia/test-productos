from django.shortcuts import render
from rest_framework import viewsets, mixins

from core.models import Category, Product
from core.serializers import (
    CategorySerializer,
    ProductDetailSerializer,
    ProductListSerializer,
    ProductPartialSerializer,
)
from users.permissions import ProductModelPermission


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

    def get_permissions(self):
        if self.action in ["update", "destroy"]:
            permission_classes = [ProductModelPermission]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.user.is_anonymous:
            return self.serializer_class
        if self.action in ["retrieve", "update"]:
            return ProductDetailSerializer
        return ProductListSerializer


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
