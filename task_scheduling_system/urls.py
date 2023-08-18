"""
URL configuration for task_scheduling_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from dj_rest_auth.views import UserDetailsView, PasswordChangeView
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, \
    SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('task_scheduling_system.authentication.api.urls')),
    path('api/v1/tasks/', include('task_scheduling_system.tasks.api.urls')),
    path('api/v1/users/', include('task_scheduling_system.users.api.urls')),
    path('api/v1/user/', include('task_scheduling_system.user.api.urls')),
    path(route='api/v1/schema/', view=SpectacularAPIView.as_view(), name='schema'),
    path(route='api/v1/schema/swagger-ui/',
         view=SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path(route='api/v1/schema/redoc/',
         view=SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
    path(route='', view=RedirectView.as_view(pattern_name='swagger-ui')),
]
