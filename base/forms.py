from django.forms import ModelForm

from .models import Player, Team, Club


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'middle_name', 'last_name', 'gender', 'license', 'birth_date']


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = '__all__'
