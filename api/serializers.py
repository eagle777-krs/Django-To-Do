from rest_framework import serializers
from tasks.models import Task, Category

class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Task
        exclude = ('category', 'user', 'status')

class UPDTaskSerializer(serializers.Serializer):
    category = serializers.ReadOnlyField(source='Category.name')
    c =serializers.ReadOnlyField(source='Category.priority')
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'created_at', 'deadline', 'category', 'category', 'status')
