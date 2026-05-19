from django.contrib import admin
from .models import Campaign, Donation

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'current_amount', 'goal_amount', 'is_active')

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'amount', 'campaign', 'status', 'date')
    list_filter = ('status', 'campaign')
    search_fields = ('donor_name', 'donor_email', 'transaction_id')
