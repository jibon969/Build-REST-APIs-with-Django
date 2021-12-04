from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from movie_stream_app.models import StreamPlatform, WatchList
from movie_stream_app.api.serialization import StreamPlatformSerializer, WatchListSerializer


# Function based view

@api_view(['GET'])
def watch_list(request):
    queryset = WatchList.objects.all()
    serializer = WatchListSerializer(queryset, many=True)
    return Response(serializer.data)

