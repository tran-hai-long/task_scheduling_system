from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer, LoginSerializer
from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes


class CustomUserAuthSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = ('id', 'email', 'username', 'full_name',)

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        setattr(instance, 'first_name', None)
        setattr(instance, 'last_name', None)
        instance.save()
        return instance


class CustomUserLoginSerializer(LoginSerializer):
    username = None


class CustomRegisterSerializer(RegisterSerializer):
    password1 = None
    password2 = None
    password = serializers.CharField(write_only=True)
    retyped_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['retyped_password']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', ''),
        }
