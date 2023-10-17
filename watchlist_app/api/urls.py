from django.urls import path
from watchlist_app.api.views import StreamPlatformAV ,StreamPlatfromDetalisAV, WatchListAV, WatchListDetailsAV


urlpatterns = [
    path('stream',StreamPlatformAV.as_view(), name='streamplatform'),
    path('stream/<int:pk>', StreamPlatfromDetalisAV.as_view(),name = 'streamplatform-detail'),
    path('list', WatchListAV.as_view(), name='watchlist'),
    path('<int:pk>', WatchListDetailsAV.as_view(), name='watchlist-detail')
]