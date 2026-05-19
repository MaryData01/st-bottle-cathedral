from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Donation, Campaign

def donate(request):
    campaigns = Campaign.objects.filter(is_active=True)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        campaign_id = request.POST.get('campaign')

        campaign = None
        if campaign_id:
            campaign = Campaign.objects.filter(id=campaign_id).first()

        Donation.objects.create(
            donor_name=name,
            donor_email=email,
            amount=amount,
            message=message,
            campaign=campaign,
            status='SUCCEEDED' # Dummy success
        )
        
        messages.success(request, 'Thank you for your generous donation!')
        return redirect('core:home')
        
    return render(request, 'donations/donate.html', {'campaigns': campaigns})
