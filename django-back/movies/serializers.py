from rest_framework import serializers
from .models import Movie, Genre, Review
from accounts.serializers import UserSerializer


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'movie_genres']

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(required=False)
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(required=False)
    user = UserSerializer(required=False)
    class Meta:
        model = Review
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(required=False)
    user = UserSerializer(required=False)
    class Meta:
        model = Review
        fields = '__all__'