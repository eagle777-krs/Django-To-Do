from django.urls import path
from .views import index, current_task, AddTaskView, EditTaskView, DeleteTaskView, updated_done_tasks

app_name = 'tasks'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', current_task, name='task'),
    path('<int:id>/edit/', EditTaskView.as_view(), name='edit_task'),
    path('<int:id>/del/', DeleteTaskView.as_view(), name='delete_task'),
    path('add/', AddTaskView.as_view(), name='add'),
    path('update/', updated_done_tasks, name='updated_done_tasks')
]