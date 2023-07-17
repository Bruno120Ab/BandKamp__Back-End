from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

from django.shortcuts import get_object_or_404

from songs.models import Song
from songs.serializers import SongSerializer
from albums.models import Album


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs["pk"])
        serializer.save(album=album)
