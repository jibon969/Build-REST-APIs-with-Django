from django.urls import path
from movie_stream_app.api.views import (
    watch_list,
)

urlpatterns = [
    path('watch-list/', watch_list, name="watch-list"),
]