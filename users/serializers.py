from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(instance.password)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "full_name",
            "artistic_name",
        ]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["is_superuser"]
