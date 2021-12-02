from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=200)
    active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = instance.validated_data.get('name', instance.name)
        instance.description = instance.validated_data.get('description', instance.description)
        instance.description = instance.validated_data.get('active', instance.active)
        instance.save()
        return instance