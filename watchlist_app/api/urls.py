from django.urls import path
from watchlist_app.api.views import StreamPlatformAV ,StreamPlatfromDetalisAV, WatchListAV, WatchListDetailsAV,ReviewList, ReviewDetail


urlpatterns = [
    path('stream',StreamPlatformAV.as_view(), name='streamplatform'),
    path('stream/<int:pk>', StreamPlatfromDetalisAV.as_view(),name = 'streamplatform-detail'),
    path('list', WatchListAV.as_view(), name='watchlist'),
    path('<int:pk>', WatchListDetailsAV.as_view(), name='watchlist-detail'),
    path('review', ReviewList.as_view(), name='review'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='watchlist-detail'),
]