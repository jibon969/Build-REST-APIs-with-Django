from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from movie_stream_app.models import StreamPlatform, WatchList
from movie_stream_app.api.serialization import StreamPlatformSerializer, WatchListSerializer


# Function based view

@api_view(['GET', 'POST'])
def watch_list(request):
    if request.method == "GET":
        queryset = WatchList.objects.all()
        serializer = WatchListSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def watch_detail(request, pk):

    if request.method == "GET":
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Errors': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Class base view


class WatchListAv(APIView):
    def get(self, request):
        queryset = WatchList.objects.all()
        serializer = WatchListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAv(APIView):
    def get(self, request, pk):
        watch = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watch)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        watch = WatchList.objects.get(pk=pk)
        watch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformAv(APIView):
    def get(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailAv(APIView):
    def get(self, request, pk):
        strem = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(strem)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        st = StreamPlatform.objects.get(pk=pk)
        st.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




