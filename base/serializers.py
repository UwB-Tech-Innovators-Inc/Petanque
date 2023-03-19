from rest_framework.serializers import ModelSerializer
from .models import Player, Team, Club

# Create your models here.


class PlayerSerializer(ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'
        ordering = ['-license']


class TeamSerializer(ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'
        ordering = ['-name']


class ClubSerializer(ModelSerializer):

    class Meta:
        model = Club
        fields = '__all__'
        ordering = ['-name']
