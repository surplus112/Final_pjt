from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list),
    path('create/', views.article_create),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/update/', views.article_update),
    path('<int:article_pk>/comments/', views.comment_list),
    path('<int:article_pk>/comments/create/', views.comment_create),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update),
]