from django.urls import path

from .views import PlayersList, PlayerCreate, TeamsList, TeamCreate

urlpatterns = [
    path('players-list/', PlayersList.as_view(), name='players_list'),
    path('player-create/', PlayerCreate.as_view(), name='player-create'),
    path('teams-list/', TeamsList.as_view(), name='teams-list'),
    path('team-create/', TeamCreate.as_view(), name='team-create')
]
