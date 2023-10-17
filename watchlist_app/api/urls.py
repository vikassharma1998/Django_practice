from django.urls import path
from watchlist_app.api.views import StreamPlatformAV ,StreamPlatfromDetalisAV, WatchListAV, WatchListDetailsAV


urlpatterns = [
    path('stream',StreamPlatformAV.as_view(), name='streamplatform-list'),
    path('stream/<int:pk>', StreamPlatfromDetalisAV.as_view(),name = 'Stream-Platfrom-Detalis'),
    path('list', WatchListAV.as_view(), name='Watch-List'),
    path('<int:pk>', WatchListDetailsAV.as_view(), name='Watch-List')
]