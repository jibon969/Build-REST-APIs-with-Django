from django.urls import path, include

urlpatterns = [
    path('api/', include('watchlist_app.api.urls')),
]
