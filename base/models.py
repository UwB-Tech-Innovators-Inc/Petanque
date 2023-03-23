import datetime
from django.db import models
from djongo.models.fields import ObjectIdField

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)

    class Gender(models.TextChoices):
        Male = "Male"
        Female = "Female"

    gender = models.CharField(max_length=6, choices=Gender.choices)

    class Meta:
        abstract = True

    def __str__(self):
        if self.middle_name is None:
            return f'{self.first_name} {self.last_name}'
        return f'{self.first_name} {self.middle_name} {self.last_name}'


class Player(Person):
    license = models.CharField(max_length=30, blank=True, null=True, unique=True)
    birth_date = models.DateField(default=datetime.date.today)
    # age_category = models.CharField(max_length=2)  # set from birth_date
    power = models.FloatField(default=0)
    points = models.FloatField(default=0)


class Address(models.Model):
    street = models.CharField(max_length=30)
    apt_suite_etc = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    postcode = models.CharField(max_length=30)

    class Meta:
        abstract = True


class Club(Address):
    _id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=30)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.name


class Team(models.Model):
    _id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=30)
    team_players = models.ManyToManyField(Player)
    desc = models.CharField(max_length=200)

    # match_points = models.IntegerField()
    # Manual enter, to method, count from mach_points:
    # gain_small_points = models.IntegerField()
    # lost_small_points = models.IntegerField()
    # buchholz_points = models.IntegerField()
    # free_match = models.BooleanField(default=False)
    # last_matches = models

    def __str__(self):
        return self.name


class Game:
    # team_1
    # team_2
    # score_1
    # score_2
    # ground num
    pass


class Round:
    # lista game
    # round num
    pass


class Tournament:
    # name
    # place
    # organizer
    # list of rounds
    pass
