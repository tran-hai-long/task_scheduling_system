from django.urls import path

from task_scheduling_system.tasks.api.views import TaskListAPIView, \
    TaskRetrieveUpdateDestroyAPIView

urlpatterns = [
    path(route='api/v1/', view=TaskListAPIView.as_view(), name='task_list_api'),
    path(route='api/v1/<int:pk>', view=TaskRetrieveUpdateDestroyAPIView.as_view(),
         name='task_retrieve_update_destroy_api'),
]
