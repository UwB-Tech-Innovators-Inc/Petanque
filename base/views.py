from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from .models import Player, Team
from .serializers import PlayerSerializer, TeamSerializer
from .forms import PlayerForm


@api_view(['GET', 'POST'])
def player_collection(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def team_collection(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)


class PlayerList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base/player_list.html'

    def get(self, request):
        queryset = Player.objects.all()
        return Response({'players': queryset})


class TeamList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base/team_list.html'

    def get(self, request):
        queryset = Team.objects.all()
        return Response({'teams': queryset})


def playerCreate(request):
    form = PlayerForm()

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('players')

    context = {'form': form}
    return render(request, 'base/player_create.html', context)

