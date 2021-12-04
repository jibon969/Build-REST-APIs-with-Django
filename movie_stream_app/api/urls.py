from django.urls import path
from movie_stream_app.api.views import (
    watch_list,
    watch_detail,
    # Class base urls
    WatchListAv,
    WatchDetailAv,
    # Steam
    StreamPlatformAv,
    StreamPlatformDetailAv
)

urlpatterns = [
    path('watch-list/', watch_list, name="watch-list"),
    path('watch-detail/<int:pk>/', watch_detail, name="watch-detail"),

    path('watchList/', WatchListAv.as_view(), name="watchList"),
    path('WatchDetail/<int:pk>/', WatchDetailAv.as_view(), name="WatchDetail"),

    path('stream/', StreamPlatformAv.as_view(), name="stream-list"),
    path('stream/<int:pk>/', StreamPlatformDetailAv.as_view(), name="stream-detail"),

]