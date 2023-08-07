from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import CustomUserSerializer
from ...authentication.models import CustomUser


class CustomUserListAPIView(ListAPIView):
    """
    Return a list of all users in the database. For admins only.
    """
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()


class CustomUserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get, update or delete a user. For admins only.
    """
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
