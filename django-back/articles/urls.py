from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list),
    path('create/', views.article_create),
    path('<int:article_pk>', views.article_detail),
    path('<int:article_pk>/update/', views.article_update),
]