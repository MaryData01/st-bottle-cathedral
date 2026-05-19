from django.contrib import admin
from .models import Event, Registration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'location')
    list_filter = ('start_time',)
    search_fields = ('title', 'location')

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'email', 'number_of_guests', 'registered_at')
    list_filter = ('event',)
    search_fields = ('name', 'email')
