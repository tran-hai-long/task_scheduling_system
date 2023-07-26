from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, \
    SpectacularRedocView

from task_scheduling_system.tasks.api.views import TaskListCreateAPIView, \
    TaskRetrieveUpdateDestroyAPIView, TodoListAPIView

urlpatterns = [
    path(route='schema/', view=SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
    path(route='tasks/', view=TaskListCreateAPIView.as_view(),
         name='task_list_create_api'),
    path(route='task/<int:pk>', view=TaskRetrieveUpdateDestroyAPIView.as_view(),
         name='task_retrieve_update_destroy_api'),
    path(route='to-do/', view=TodoListAPIView.as_view(), name='todo_list_api'),
]
