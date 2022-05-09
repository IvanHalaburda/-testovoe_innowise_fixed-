from customuser.models import User
from customuser.serializers import CustomUserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class CustomUserCreateView(generics.CreateAPIView):
    """
    Creation of custom user

    """
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny, )
