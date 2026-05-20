from django.db import models
from django.conf import settings
from campuses.models import Campus

class GroupCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Group Categories'

    def __str__(self):
        return self.name

class MinistryGroup(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(GroupCategory, on_delete=models.SET_NULL, null=True, related_name='groups')
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True, blank=True, related_name='groups')
    meeting_schedule = models.CharField(max_length=200, help_text="e.g., Every Tuesday at 7 PM")
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='led_groups')
    max_capacity = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GroupMembership(models.Model):
    ROLE_CHOICES = (
        ('MEMBER', 'Member'),
        ('CO_LEADER', 'Co-Leader'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='group_memberships')
    group = models.ForeignKey(MinistryGroup, on_delete=models.CASCADE, related_name='memberships')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='MEMBER')
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'group')

    def __str__(self):
        return f"{self.user.username} in {self.group.name}"
