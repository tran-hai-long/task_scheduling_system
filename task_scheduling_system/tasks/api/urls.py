from django.urls import path

from task_scheduling_system.tasks.api.views import TaskListCreateAPIView, \
    TaskRetrieveUpdateDestroyAPIView, TodoListAPIView

urlpatterns = [
    path(route='tasks/', view=TaskListCreateAPIView.as_view(),
         name='task_list_create_api'),
    path(route='task/<int:pk>', view=TaskRetrieveUpdateDestroyAPIView.as_view(),
         name='task_retrieve_update_destroy_api'),
    path(route='to-do/', view=TodoListAPIView.as_view(), name='todo_list_api'),
]
