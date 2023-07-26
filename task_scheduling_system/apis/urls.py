from django.urls import include, path

urlpatterns = [
    path('v1/tasks/', include('task_scheduling_system.tasks.api.urls')),
]
