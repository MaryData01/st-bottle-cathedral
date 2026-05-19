from django.shortcuts import render, get_object_or_404
from .models import Sermon

def sermon_list(request):
    sermons = Sermon.objects.all()
    return render(request, 'sermons/sermon_list.html', {'sermons': sermons})

def sermon_detail(request, pk):
    sermon = get_object_or_404(Sermon, pk=pk)
    return render(request, 'sermons/sermon_detail.html', {'sermon': sermon})
