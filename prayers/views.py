from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PrayerRequest

def prayer_wall(request):
    prayers = PrayerRequest.objects.filter(is_public=True)
    return render(request, 'prayers/prayer_wall.html', {'prayers': prayers})

def submit_prayer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        is_public = request.POST.get('is_public') == 'on'
        
        PrayerRequest.objects.create(
            name=name,
            email=email,
            content=content,
            is_public=is_public
        )
        messages.success(request, 'Your prayer request has been submitted.')
        return redirect('prayers:prayer_wall')
        
    return render(request, 'prayers/submit_prayer.html')
