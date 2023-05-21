from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import PlayerCreationForm, PlayerChangeForm
from .models import Player


class PlayerAdmin(UserAdmin):
    add_form = PlayerCreationForm
    form = PlayerChangeForm
    model = Player
    list_display = ["username", "email", ]

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('gender', 'license', 'birth_date', 'age_category', 'power', 'points')
        })
    )


admin.site.register(Player, PlayerAdmin)
