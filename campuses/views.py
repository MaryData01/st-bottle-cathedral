from django.shortcuts import render
from .models import Campus

def campus_list(request):
    campuses = Campus.objects.filter(is_active=True)
    return render(request, 'campuses/campus_list.html', {'campuses': campuses})
