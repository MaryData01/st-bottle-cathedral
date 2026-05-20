from django.contrib import admin
from .models import Campus

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('name', 'timezone', 'main_pastor', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_active', 'timezone')
    search_fields = ('name', 'address')
