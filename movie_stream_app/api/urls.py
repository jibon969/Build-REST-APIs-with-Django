from django.urls import path
from movie_stream_app.api.views import (
    watch_list,
    watch_detail
)

urlpatterns = [
    path('watch-list/', watch_list, name="watch-list"),
    path('watch-detail/<int:pk>/', watch_detail, name="watch-detail"),
]