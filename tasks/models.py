from django.db import models
from django.db.models import CASCADE


class Priority(models.TextChoices):
    LOW = 'low', 'Low'
    MEDIUM = 'medium', 'Medium'
    HIGH = 'high', 'High'

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.LOW)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(default=None)
    category = models.ForeignKey(Category, on_delete=CASCADE)

    def __str__(self):
        return self.name
