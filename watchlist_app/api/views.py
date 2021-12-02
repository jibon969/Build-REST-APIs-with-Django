from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serialization import MovieSerializer


@api_view(['GET'])
def movie_list(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)