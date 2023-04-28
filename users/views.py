from rest_framework import viewsets, mixins
from django.contrib.auth.models import User

from users.serializer import UserSerializer, UserRegisterSerializer


class UserViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegisterSerializer
        return self.serializer_class
