# Generated by Django 4.1.7 on 2023-03-10 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_team_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='user',
        ),
        migrations.RemoveField(
            model_name='team',
            name='user',
        ),
    ]
