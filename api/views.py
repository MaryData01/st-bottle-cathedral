from rest_framework import viewsets
from campuses.models import Campus
from groups.models import MinistryGroup
from events.models import Event
from sermons.models import Sermon
from .serializers import CampusSerializer, MinistryGroupSerializer, EventSerializer, SermonSerializer

class CampusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Campus.objects.filter(is_active=True)
    serializer_class = CampusSerializer

class MinistryGroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MinistryGroup.objects.filter(is_active=True)
    serializer_class = MinistryGroupSerializer

class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all().order_by('start_time')
    serializer_class = EventSerializer

class SermonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sermon.objects.all().order_by('-date')
    serializer_class = SermonSerializer
