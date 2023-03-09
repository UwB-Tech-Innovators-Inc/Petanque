from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Player, Team


class PlayersList(ListView):
    model = Player


class PlayerCreate(CreateView):
    model = Player
    fields = ['first_name', 'last_name', 'license']
    success_url = reverse_lazy('players_list')


class TeamsList(ListView):
    model = Team


class TeamCreate(CreateView):
    model = Team
    fields = ['name', 'club', 'players', 'date', 'desc']
    success_url = reverse_lazy('teams_list')

