from rest_framework import generics
from .serializers import TaskSerializer
from ..models import Task


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
