from allauth.account.views import ConfirmEmailView
from django.urls import include, path
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, \
    SpectacularSwaggerView

urlpatterns = [
    path('tasks/', include('task_scheduling_system.tasks.api.urls')),
    path('users/', include('task_scheduling_system.users.api.urls')),
    path(route='schema/', view=SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('confirm-email/<str:key>/', ConfirmEmailView.as_view(),
         name='account_confirm_email'),
    path('account-email/', RedirectView.as_view(pattern_name='rest_login'),
         name='account_email'),
    path('login-redirect', RedirectView.as_view(pattern_name='rest_login'),
         name='account_login'),  # TODO: redirect to account_profile
    path('logout-redirect', RedirectView.as_view(pattern_name='rest_logout'),
         name='account_logout'),
    path('signup-redirect', RedirectView.as_view(pattern_name='rest_register'),
         name='account_signup')
]
