from django.contrib import admin
from .models import GroupCategory, MinistryGroup, GroupMembership

@admin.register(GroupCategory)
class GroupCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MinistryGroup)
class MinistryGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'campus', 'leader', 'is_active')
    list_filter = ('category', 'campus', 'is_active')
    search_fields = ('name', 'description')

@admin.register(GroupMembership)
class GroupMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'role', 'joined_at')
    list_filter = ('role', 'group')
