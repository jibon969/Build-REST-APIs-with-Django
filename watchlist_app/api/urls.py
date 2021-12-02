from django.urls import path
from watchlist_app.api.views import (
    movie_list,
    movie_detail,

    # Detail Views
    MovieListView,
    MovieDetailView
)


urlpatterns = [
    path('list/', movie_list, name="movie-list"),
    path('list/<int:pk>/', movie_detail, name="movie-detail"),

    # Class based view urls
    path("list-view/", MovieListView.as_view(), name="list-view"),
    path("list-view/", MovieDetailView.as_view(), name="list-view")
]

