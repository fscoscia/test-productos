from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import UserProfile
from django.contrib.auth.password_validation import validate_password


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
