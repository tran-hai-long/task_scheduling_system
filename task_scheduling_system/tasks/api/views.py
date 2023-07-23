from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .serializers import TaskSerializer
from ..models import Task


class TaskListAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
