from rest_framework import serializers
from core.models import Product, Category, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("id", "image")


class ProductPartialSerializer(serializers.ModelSerializer):
    state = serializers.CharField(source="get_state_display")

    class Meta:
        model = Product
        fields = ("id", "name", "state")


class ProductListSerializer(ProductPartialSerializer):
    categories = CategorySerializer(many=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ("created_at", "updated_at")

    def get_images(self, obj):
        request = self.context["request"]
        if obj.images.exists():
            return request.build_absolute_uri(obj.images.first().image.url)
        return None


class ProductDetailSerializer(ProductListSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
