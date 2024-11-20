from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, OrdemServico

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'full_name', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('full_name',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OrdemServico)