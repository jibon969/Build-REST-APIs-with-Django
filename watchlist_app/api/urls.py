from django.urls import path
from watchlist_app.api.views import movie_list, movie_detail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('list/', movie_list, name="movie-list"),
    path('<int:pk>/', movie_detail, name="movie-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
