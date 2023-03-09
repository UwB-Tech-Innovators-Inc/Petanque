from django.urls import path

from .views import PlayerList, PlayerCreate

urlpatterns = [
    path('', PlayerList.as_view(), name='players'),
    path('player-create/', PlayerCreate.as_view(), name='player-create'),
]
