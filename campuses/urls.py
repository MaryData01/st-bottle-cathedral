from django.urls import path
from . import views

app_name = 'campuses'

urlpatterns = [
    path('', views.campus_list, name='campus_list'),
]
