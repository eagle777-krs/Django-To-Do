from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User


class Priority(models.TextChoices):
    LOW = 'Низкий', 'Низкий'
    MEDIUM = 'Медиум (средний)', 'Медиум (средний)'
    HIGH = 'Высокий', 'Высокий'

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.LOW)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(default=None)
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name='tasks')
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='tasks')
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['status','deadline', '-category']


    def __str__(self):
        return self.name
