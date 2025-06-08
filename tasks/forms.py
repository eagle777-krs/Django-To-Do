from django import forms
from .models import Task

class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'deadline', 'category', 'status']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'name': 'Название задачи',
            'description': 'Описание',
            'created_at': 'Дата создания',
            'deadline': 'Дедлайн',
            'category': 'Категория',
            'status': 'Статус',
        }

class TaskAddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'deadline', 'category']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'name': 'Название задачи',
            'description': 'Описание',
            'deadline': 'Дедлайн',
            'category': 'Категория',
        }