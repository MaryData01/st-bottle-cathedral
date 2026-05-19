from django.shortcuts import render
from sermons.models import Sermon
from events.models import Event

def home(request):
    latest_sermons = Sermon.objects.all()[:3]
    upcoming_events = Event.objects.all()[:3]
    return render(request, 'core/home.html', {
        'latest_sermons': latest_sermons,
        'upcoming_events': upcoming_events
    })

def about(request):
    return render(request, 'core/about.html')
