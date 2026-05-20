from django.contrib import admin
from .models import MinistryTeam, TeamRole, VolunteerProfile, ServiceSchedule, ScheduleAssignment

@admin.register(MinistryTeam)
class MinistryTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'campus')
    list_filter = ('campus',)

@admin.register(TeamRole)
class TeamRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'team')
    list_filter = ('team',)

@admin.register(VolunteerProfile)
class VolunteerProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'skills')

@admin.register(ServiceSchedule)
class ServiceScheduleAdmin(admin.ModelAdmin):
    list_display = ('date', 'event')
    list_filter = ('date',)

@admin.register(ScheduleAssignment)
class ScheduleAssignmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'schedule', 'role', 'status')
    list_filter = ('status', 'schedule__date')
