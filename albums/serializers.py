from rest_framework import serializers

from albums.models import Album

from users.serializers import UserSerializer


class AlbumSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Album
        fields = ["id", "name", "year", "user"]
        read_only_fields = ["user_id"]
