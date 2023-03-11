from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    license = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.license}'


class Team(models.Model):
    name = models.CharField(max_length=30, unique=True)
    club = models.CharField(max_length=30)
    players = models.ManyToManyField(Player)
    date = models.DateField(default=datetime.date.today)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name
