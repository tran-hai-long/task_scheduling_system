from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from ..models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ['password']
        read_only_fields = ["last_login", "date_joined", "email"]
