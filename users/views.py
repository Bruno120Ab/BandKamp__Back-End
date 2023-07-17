from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsAccountOwner


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
