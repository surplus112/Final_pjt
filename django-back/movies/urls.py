from django.urls import path
from . import views

app_names = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('create/', views.movie_create),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/update/', views.movie_update),
    path('<int:movie_pk>/reviews/', views.review_list),
    path('<int:movie_pk>/reviews/create/', views.review_create),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_update),
]