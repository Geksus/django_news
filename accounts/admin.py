from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ["username", "email", "age", "is_staff", "is_superuser", "address"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age", "address")}),)


admin.site.register(CustomUser, CustomUserAdmin)
