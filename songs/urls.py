from django.urls import path

from .views import SongView

urlpatterns = [
    path("songs/<int:pk>/", SongView.as_view()),
]
