from django.shortcuts import render
from .models import MinistryGroup

def group_list(request):
    groups = MinistryGroup.objects.filter(is_active=True).select_related('campus', 'category')
    return render(request, 'groups/group_list.html', {'groups': groups})
