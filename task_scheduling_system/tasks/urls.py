from django.urls import path

from task_scheduling_system.tasks.api.views import TaskListAPIView

urlpatterns = [path(route='api/v1/', view=TaskListAPIView.as_view(), name='task_list_api')]
