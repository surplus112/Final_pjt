from django.urls import path
from . import views

app_names = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('create/', views.movie_create),
    path('<int:movie_pk>', views.movie_detail),
]