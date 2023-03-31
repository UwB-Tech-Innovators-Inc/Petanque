from django.urls import path
from django.contrib.auth.views import LogoutView
# from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('players/', views.PlayerList.as_view(), name='players'),
    path('create-player/', views.playerCreate, name='create-player'),
    path('teams/', views.TeamList.as_view(), name='teams'),
    path('create-team/', views.teamCreate, name='create-team'),
    path('clubs/', views.ClubList.as_view(), name='clubs'),
    path('create-club/', views.clubCreate, name='create-club'),

    path('login/', views.CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
]
