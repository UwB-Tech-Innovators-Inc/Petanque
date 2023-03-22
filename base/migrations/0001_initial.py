# Generated by Django 4.1.7 on 2023-03-22 08:11

import datetime
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('license', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('birth_date', models.DateField(default=datetime.date.today)),
                ('power', models.FloatField(default=0)),
                ('points', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=200)),
                ('team_players', models.ManyToManyField(to='base.player')),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=30)),
                ('apt_suite_etc', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('postcode', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('players', models.ManyToManyField(to='base.player')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
