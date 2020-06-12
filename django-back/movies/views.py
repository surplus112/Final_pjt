from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import MovieSerializer, MovieListSerializer, GenreSerializer
from .models import Movie, Genre


# Create your views here.
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
        return Response({'message':'Comment has been deleted!'})





# @api_view(['GET'])
# def movie_detail(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data)

# @api_view(['PUT'])
# @permission_classes([IsAdminUser])
# def movie_update(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     serializer = MovieSerializer(data=request.data, instance=movie)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data)

# @api_view(['DELETE'])
# @permission_classes([IsAdminUser])
# def movie_delete(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     movie.delete()
#     return HttpResponse(status=200)