from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework.serializers import raise_errors_on_nested_writes


class CustomUserSerializer(UserDetailsSerializer):
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
