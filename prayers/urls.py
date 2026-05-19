from django.urls import path
from . import views

app_name = 'prayers'

urlpatterns = [
    path('', views.prayer_wall, name='prayer_wall'),
    path('submit/', views.submit_prayer, name='submit_prayer'),
]
