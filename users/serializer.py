from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import UserProfile
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "password")

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        profile = UserProfile.objects.create(user=user)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    approved = serializers.BooleanField(source="profile.approved")

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "approved")


class ObtainTokenSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, min_length=3)
    password = serializers.CharField(write_only=True, min_length=4)
    access_token = serializers.CharField(read_only=True)
    token_type = serializers.CharField(default="Bearer", read_only=True)

    def validate(self, attrs):
        super().validate(attrs)
        user = authenticate(
            username=attrs["username"],
            password=attrs["password"],
        )
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        attrs["user"] = user
        refresh = RefreshToken.for_user(user)
        attrs["access_token"] = str(refresh.access_token)
        return attrs
