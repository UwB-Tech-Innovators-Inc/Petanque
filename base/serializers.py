from rest_framework import serializers
from .models import Player, Team, Club, Tournament

# Create your models here.


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'
        ordering = ['-license']


class ClubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = '__all__'
        ordering = ['-name']


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class TournamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = '__all__'
