from allauth.account.views import ConfirmEmailView
from allauth.socialaccount.providers.github import views as github_views
from django.urls import path, include
from django.views.generic import RedirectView

from ..api.views import GithubLoginView, github_callback

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('confirm-email/<str:key>/', ConfirmEmailView.as_view(),
         name='account_confirm_email'),
    path('account-email/', RedirectView.as_view(pattern_name='rest_login'),
         name='account_email'),
    path('login-redirect', RedirectView.as_view(pattern_name='rest_user_details'),
         name='account_login'),
    path('logout-redirect', RedirectView.as_view(pattern_name='rest_logout'),
         name='account_logout'),
    path('signup-redirect', RedirectView.as_view(pattern_name='rest_register'),
         name='account_signup'),
    path(route='github/', view=GithubLoginView.as_view(), name='github_login'),
    path(route='github/url/', view=github_views.oauth2_login,
         name='github_login_redirect'),
    path(route='github/callback/', view=github_callback, name='github_callback'),
]
