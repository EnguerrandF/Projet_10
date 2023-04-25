from rest_framework import serializers
from authentication.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['password', 'username', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
