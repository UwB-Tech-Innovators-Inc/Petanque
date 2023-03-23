from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from .models import Player, Team, Club
from .serializers import PlayerSerializer, TeamSerializer, ClubSerializer
from .forms import PlayerForm, TeamForm, ClubForm


def home(request):
    return render(request, 'base/home.html')


@api_view(['GET'])
def player_collection(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)


class PlayerList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base/player_list.html'

    def get(self, request):
        queryset = Player.objects.all()
        return Response({'players': queryset})


def playerCreate(request):
    form = PlayerForm()

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('players')

    context = {'form': form}
    return render(request, 'base/player_create.html', context)


@api_view(['GET'])
def team_collection(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)


class TeamList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base/team_list.html'

    def get(self, request):
        queryset = Team.objects.all()
        return Response({'teams': queryset})


def teamCreate(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.save()
            team_players = form.cleaned_data.get('team_players') or []
            for player in team_players:
                team.team_players.add(player)
            return redirect('teams')
    else:
        form = TeamForm()
    return render(request, 'base/team_create.html', {'form': form})


@api_view(['GET'])
def club_collection(request):
    if request.method == 'GET':
        clubs = Club.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)


class ClubList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base/club_list.html'

    def get(self, request):
        queryset = Club.objects.all()
        return Response({'clubs': queryset})


def clubCreate(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            club = form.save(commit=False)
            club.save()
            players = form.cleaned_data.get('players') or []
            for player in players:
                club.players.add(player)
            return redirect('clubs')
    else:
        form = ClubForm()
    return render(request, 'base/club_create.html', {'form': form})
