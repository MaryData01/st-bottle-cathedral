from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampusViewSet, MinistryGroupViewSet, EventViewSet, SermonViewSet

router = DefaultRouter()
router.register(r'campuses', CampusViewSet)
router.register(r'groups', MinistryGroupViewSet)
router.register(r'events', EventViewSet)
router.register(r'sermons', SermonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
