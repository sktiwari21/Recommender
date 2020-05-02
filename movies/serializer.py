from rest_framework import serializers
from recommender.movies.models import Movies

# Movie Serializer
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'
