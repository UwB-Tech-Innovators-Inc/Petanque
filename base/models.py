from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    license = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-license']


class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30, unique=True)
    club = models.CharField(max_length=30)
    players = models.ManyToManyField(Player)
    date = models.DateField(default=datetime.date.today)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']
