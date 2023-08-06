from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import CustomUserSerializer
from ..models import CustomUser


class CustomUserListAPIView(ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()


class CustomUserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
