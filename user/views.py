from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import FormView, CreateView
from django.urls import reverse_lazy

from .models import Player
from .forms import PlayerCreationForm


def account_details(request):
    user = Player.objects.get(username=request.user)
    context = {'user': user}
    return render(request, 'user/account.html', context)


class LoginView(LoginView):
    template_name = "user/login.html"


class SignUpView(CreateView):
    form_class = PlayerCreationForm
    success_url = reverse_lazy("login")
    template_name = "user/signup.html"
