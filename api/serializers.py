from rest_framework import serializers
from tasks.models import Task, Category

class TaskSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    created_at = serializers.DateField()
    deadline = serializers.DateField()
    category = serializers.CharField(source='category.field', max_length=100)
    username = serializers.CharField(source='user.username', max_length=100)

class UPDTaskSerializer(serializers.Serializer):
    category = serializers.ReadOnlyField(source='Category.name')
    c =serializers.ReadOnlyField(source='Category.priority')
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'deadline', 'category', 'category', 'status']
