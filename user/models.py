import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class Player(AbstractUser):
    class Gender(models.TextChoices):
        Male = "Male"
        Female = "Female"

    gender = models.CharField(max_length=6, choices=Gender.choices)
    license = models.CharField(max_length=30, blank=True, null=True, unique=True)
    birth_date = models.DateField(default=datetime.date.today)
    age_category = models.CharField(max_length=2)  # set from birth_date
    power = models.FloatField(default=0)
    points = models.FloatField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.license}'
