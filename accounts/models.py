from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    is_member = models.BooleanField(default=False)
    home_campus = models.ForeignKey('campuses.Campus', on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    
    # Predefined Roles
    is_campus_pastor = models.BooleanField(default=False)
    is_group_leader = models.BooleanField(default=False)
    is_volunteer_coordinator = models.BooleanField(default=False)

    def __str__(self):
        return self.username
