from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, \
    ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import TaskSerializer
from ..models import Task


class TaskListCreateAPIView(ListCreateAPIView):
    """
    Return a list of all tasks created by the logged-in user. User can also POST to
    create a new task.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Task.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        if not is_many:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['user'] = self.request.user
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            for task in serializer.validated_data:
                task['user'] = self.request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get, update or delete a task created by the logged-in user.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Task.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = self.request.user
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class TodoListAPIView(ListAPIView):
    """
    Return a list of all to-do tasks belong to the logged-in user.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Task.objects.filter(user=self.request.user, to_do=True)
