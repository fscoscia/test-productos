from django.shortcuts import render
from rest_framework import viewsets, mixins

from core.models import Product
from core.serializers import ProductFullSerializer, ProductPartialSerializer


class ProductViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Product.objects.all()
    serializer_class = ProductPartialSerializer

    def get_serializer_class(self):
        if self.request.user.is_anonymous:
            return self.serializer_class
        return ProductFullSerializer
