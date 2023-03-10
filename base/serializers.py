from rest_framework import serializers
from .models import Player, Team

# Create your models here.


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'license')
        ordering = ['-license']


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('name', 'club', 'players', 'date', 'desc')
        ordering = ['-date']
