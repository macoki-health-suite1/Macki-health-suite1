from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class MaCoKiUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("MaCoKi", {"fields": ("organisation", "facility", "role")}),)
    list_display = ("username", "role", "organisation", "is_active")
