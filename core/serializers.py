from rest_framework import serializers

from core.models import Product


class ProductPartialSerializer(serializers.ModelSerializer):
    state = serializers.CharField(source="get_state_display")

    class Meta:
        model = Product
        fields = ("name", "state")


class ProductFullSerializer(serializers.ModelSerializer):
    state = serializers.CharField(source="get_state_display")

    class Meta:
        model = Product
        exclude = ("created_at", "updated_at")
