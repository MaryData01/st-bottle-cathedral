from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_member']
    fieldsets = UserAdmin.fieldsets + (
        ('Church Details', {'fields': ('phone_number', 'address', 'is_member')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
