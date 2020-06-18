from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import MovieSerializer, MovieListSerializer, GenreSerializer, ReviewSerializer, ReviewListSerializer
from .models import Movie, Genre, Review


# Create your views here.
@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def movie_create(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def movie_update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'PUT':
        serializer = MovieSerializer(data=request.data, instance=movie)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        movie.delete()
        return Response({'message': 'Movie has been deleted!'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_reviews(request, user_name):
    if request.user.username == user_name:
        reviews = Review.objects.filter(user=request.user.id)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        return Response({'message': 'You do not have permission!'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_movie(request, user_name):
    if request.user.username == user_name:
        # request user's reviews
        reviews = Review.objects.filter(user=request.user.id)
        # number of reviews less than 3
        if len(reviews) < 3:
            # random
            movies = Movie.objects.order_by("?")[:12]
            serializer = MovieListSerializer(movies, many=True)
            return Response(serializer.data)
        else:
            movie_dict = {}
            for review in reviews:
                movies = Movie.objects.filter(pk=review.movie_id)
                serializer = MovieListSerializer(movies, many=True)
                # genre count
                for movie in serializer.data:
                    for genre in movie['genres']:
                        if genre not in movie_dict:
                            movie_dict[genre] = 1
                        else:
                            movie_dict[genre] += 1
            # sort genre
            movies_arr = sorted(movie_dict.items(), key= lambda x: -x[1])
            # the most seleted genre
            genre = Genre.objects.filter(pk=movies_arr[0][0])
            genre_serializer = GenreSerializer(genre, many=True)
            # Search for a movie that corresponds to the genre
            recommend = genre_serializer.data[0]['movie_genres']
            recommend = recommend[:12]
            movies = Movie.objects.filter(id__in=recommend)
            serializer = MovieListSerializer(movies, many=True)
            return Response(serializer.data)
    else:
        return Response({'message': 'You do not have permission!'})

@api_view(['GET'])
def review_list(request, movie_pk):
    reviews = Review.objects.filter(movie=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_update(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user.id == review.user.id:
        if request.method == 'PUT':
            serializer = ReviewSerializer(data=request.data, instance=review)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            review.delete()
            return Response({'message': 'Review has been deleted!'})
    else:
        return Response({'message': 'Author only'})