from django import forms

from .models import Player, Team, Club, Tournament


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'middle_name', 'last_name', 'gender', 'license', 'birth_date']


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'
