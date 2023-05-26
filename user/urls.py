from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('account/', login_required(views.account_details), name='account'),
]
