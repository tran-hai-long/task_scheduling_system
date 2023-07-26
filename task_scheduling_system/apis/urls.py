from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, \
    SpectacularSwaggerView

urlpatterns = [
    path('tasks/', include('task_scheduling_system.tasks.api.urls')),
    path(route='schema/', view=SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
    path('auth/', include('dj_rest_auth.urls')),
]
