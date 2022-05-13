from customuser.models import User
from customuser.serializers import CustomUserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated


class CustomUserCreateView(generics.CreateAPIView):
    """
    Creation of custom user

    """
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny, )


class CustomUserListView(generics.ListAPIView):
    """
    list of all users

    """
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated, )
