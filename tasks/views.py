from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from .models import Task, Status
from .forms import TaskAddForm, TaskEditForm

def index(request):
    top_10_tasks = Task.objects.order_by('deadline')\
    .filter(user_id=request.user.id, status=Status.UNDONE.value).all()[:10]
    context = {'tasks':top_10_tasks}
    return render(
        request,
        'index.html',
        context
    )

class AddTaskView(View):

    def get(self, request):
        form = TaskAddForm()
        context = {'form':form}
        return render(request, 'add_task.html', context)

    def post(self, request):
        form = TaskAddForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.status = Status.UNDONE
            task.save()
            return redirect(reverse('tasks:index'))
        context = {'form':form}
        return render(request, 'add_task.html', context)

class EditTaskView(View):

    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        form = TaskEditForm(instance=task)
        context = {'form':form}
        return render(request, 'edit_task.html', context)

    def post(self, request, id):
        task = get_object_or_404(Task, id=id)
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(reverse('tasks:index'))
        context = {'form':form}
        return render(request, 'edit_task.html', context)

class DeleteTaskView(View):

    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        context = {'task':task}
        return render(request, 'delete_task.html', context)

    def post(self, request, id):
        task = get_object_or_404(Task, id=id)
        task.delete()
        return redirect(reverse('tasks:index'))

def current_task(request, id):
    task = Task.objects.get(id=id)
    context = {'task':task}
    return render(request, 'current_task.html', context)

