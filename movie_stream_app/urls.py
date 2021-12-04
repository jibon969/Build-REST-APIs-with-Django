from django.urls import path, include

urlpatterns = [
    path('api/', include('movie_stream_app.api.urls')),
]