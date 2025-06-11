from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from tasks.models import Task
from .serializers import TaskSerializer, UPDTaskSerializer

class GetTaskInfoView(APIView):

    def get(self, request):

        queryset = Task.objects.all()

        serializer = TaskSerializer(instance=queryset, many=True)
        return Response(serializer.data)

# В отличие от файла serializer_example_2.py,
# где мы явно прописывали json-рендер и вызывали у него метод render, в коде контроллера ничего такого нет.
# Но рендер всё равно отработает: его работа описана под капотом внутри класса-родителя APIView.

class GetMoreTaskInfoView(APIView):

    def post(self, request):
        serializer = UPDTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
