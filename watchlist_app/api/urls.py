from django.urls import path
from watchlist_app.api.views import MovieListAV, MovieDetailsAV


urlpatterns = [
    path('movie-list',MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>',MovieDetailsAV.as_view(), name='movie-detail'),
]