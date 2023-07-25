from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, \
    SpectacularRedocView

from task_scheduling_system.tasks.api.views import TaskListCreateAPIView, \
    TaskRetrieveUpdateDestroyAPIView, TodoListAPIView

urlpatterns = [
    path(route='api/schema/', view=SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
    path(route='api/v1/tasks/', view=TaskListCreateAPIView.as_view(),
         name='task_list_create_api'),
    path(route='api/v1/task/<int:pk>', view=TaskRetrieveUpdateDestroyAPIView.as_view(),
         name='task_retrieve_update_destroy_api'),
    path(route='api/v1/to-do', view=TodoListAPIView.as_view(), name='todo_list_api'),
]
