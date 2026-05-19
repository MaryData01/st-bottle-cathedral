from django.contrib import admin
from .models import Speaker, Series, Sermon

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'speaker', 'series')
    list_filter = ('speaker', 'series', 'date')
    search_fields = ('title', 'passage')
