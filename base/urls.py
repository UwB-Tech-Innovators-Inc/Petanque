from django.urls import path

from . import views


urlpatterns = [
    path('players/', views.PlayerList.as_view(), name='players'),
    path('create-player/', views.playerCreate, name='create-player'),
    path('teams/', views.TeamList.as_view(), name='teams'),
]
