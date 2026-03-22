from django.shortcuts import render, get_object_or_404
from .models import SystemGeneration
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def hubs_list(request):
    generations = SystemGeneration.generations.all()
    return render(request, 'obj_hub/list.html', {'generations': generations})

@login_required(login_url='login')
def hub_detail(request, pk):
    generation = get_object_or_404(SystemGeneration, pk=pk)
    return render(request, 'obj_hub/detail.html', {'generation': generation})