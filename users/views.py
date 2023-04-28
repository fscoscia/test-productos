from rest_framework import viewsets, mixins
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from users.serializer import (
    ObtainTokenSerializer,
    UserSerializer,
    UserRegisterSerializer,
)


class UserViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegisterSerializer
        return self.serializer_class

    @action(["post"], False, "token", "obtain_token", permission_classes=[AllowAny])
    def obtain_token(self, request, **kwargs):
        serializer = ObtainTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
