from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from .models import Task
from .forms import TaskAddForm, TaskEditForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector, SearchQuery


@login_required
def index(request):
    filter_tasks = request.GET.get('filter', 'all')
    if filter_tasks == 'done':
        tasks = Task.objects.filter(user=request.user, status=True)
    elif filter_tasks == 'undone':
        tasks = Task.objects.filter(user=request.user, status=False)
    else:
        tasks = Task.objects.filter(user=request.user)

    query = request.GET.get('search_value', '')
    if query:
        vector = SearchVector('name', 'description')
        search_query = SearchQuery(query)
        tasks = tasks.annotate(search=vector).filter(search=search_query)

    paginator = Paginator(tasks, 8)
    page_number = request.GET.get('page', 1)
    tasks = paginator.get_page(int(page_number))

    context = {'tasks':tasks, 'filter':filter_tasks, 'query':query}
    return render(
        request,
        'index.html',
        context
    )

class AddTaskView(LoginRequiredMixin, View):

    def get(self, request):
        form = TaskAddForm()
        context = {'form':form}
        return render(request, 'add_task.html', context)

    def post(self, request):
        form = TaskAddForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect(reverse('tasks:index'))
        context = {'form':form}
        return render(request, 'add_task.html', context)

class EditTaskView(LoginRequiredMixin, View):

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

class DeleteTaskView(LoginRequiredMixin, View):

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

@login_required
@require_POST
def updated_done_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    for task in tasks:
        checkbox_value = request.POST.get(f'status_{task.id}')
        task.status = True if checkbox_value else False
        task.save()
    return redirect(reverse('tasks:index'))

