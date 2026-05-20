from django.db import models
from django.conf import settings
from campuses.models import Campus
from events.models import Event

class MinistryTeam(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='ministry_teams')

    def __str__(self):
        return f"{self.name} - {self.campus.name}"

class TeamRole(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(MinistryTeam, on_delete=models.CASCADE, related_name='roles')

    def __str__(self):
        return f"{self.name} ({self.team.name})"

class VolunteerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='volunteer_profile')
    skills = models.TextField(blank=True, help_text="List of skills (e.g., Guitar, Sound engineering)")
    availability = models.TextField(blank=True, help_text="e.g., Sundays only, Twice a month")
    teams = models.ManyToManyField(MinistryTeam, blank=True, related_name='volunteers')

    def __str__(self):
        return f"{self.user.username}'s Volunteer Profile"

class ServiceSchedule(models.Model):
    date = models.DateField()
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        event_name = self.event.title if self.event else "No specific event"
        return f"{self.date} - {event_name}"

class ScheduleAssignment(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('DECLINED', 'Declined'),
    )

    schedule = models.ForeignKey(ServiceSchedule, on_delete=models.CASCADE, related_name='assignments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignments')
    role = models.ForeignKey(TeamRole, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.user.username} - {self.role} on {self.schedule.date}"
