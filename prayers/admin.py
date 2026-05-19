from django.contrib import admin
from .models import PrayerRequest

@admin.register(PrayerRequest)
class PrayerRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_submitted', 'is_public', 'is_answered')
    list_filter = ('is_public', 'is_answered', 'date_submitted')
    search_fields = ('name', 'email', 'content')
