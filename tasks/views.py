from django.shortcuts import render
from .models import Task

def index(request):
    top_10_tasks = Task.objects.order_by('created_at').all()[:10]
    context = {'tasks':top_10_tasks}
    return render(
        request,
        'index.html',
        context
    )