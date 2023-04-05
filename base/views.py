from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from .models import Player, Team, Club, Tournament
from .serializers import PlayerSerializer, TeamSerializer, ClubSerializer, TournamentSerializer
from .forms import PlayerForm, TeamForm, ClubForm, TournamentForm


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


class CustomLogin(LoginView):
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_succesful_url(self):
        return redirect('home')


class RegisterPage(FormView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)


class TournamentList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base/tournament_list.html'

    def get(self, request):
        queryset = Tournament.objects.all()
        return Response({'tournaments': queryset})
