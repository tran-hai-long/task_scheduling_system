from rest_framework.serializers import ModelSerializer

from ..models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ['password']
        read_only_fields = ["last_login", "date_joined", "email"]
