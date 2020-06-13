from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment

# Create your views here.
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'PUT':
        serializer = ArticleSerializer(data=request.data, instance=article)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            movie.delete()
            return Response({'message':'Article has been deleted!'})