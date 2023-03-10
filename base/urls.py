from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r'^api/v1/players/$', views.PlayerList.as_view()),
    re_path(r'^api/v1/teams/$', views.TeamList.as_view()),
]
