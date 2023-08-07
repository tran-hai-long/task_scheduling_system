from allauth.account.views import ConfirmEmailView
from allauth.socialaccount.providers.github import views as github_views
from allauth.socialaccount.providers.google import views as google_views
from dj_rest_auth.registration.views import SocialAccountListView, \
    SocialAccountDisconnectView
from django.urls import path, include
from django.views.generic import RedirectView

from ..api.views import GithubLoginView, github_callback, GithubConnectView, \
    GoogleLoginView, google_callback, GoogleConnectView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path(route='confirm-email/<str:key>/', view=ConfirmEmailView.as_view(),
         name='account_confirm_email'),
    # Allauth url shenanigans
    path(route='account-email/', view=RedirectView.as_view(pattern_name='rest_login'),
         name='account_email'),
    path(route='login-redirect/',
         view=RedirectView.as_view(pattern_name='rest_user_details'),
         name='account_login'),
    path(route='logout-redirect/',
         view=RedirectView.as_view(pattern_name='rest_logout'),
         name='account_logout'),
    path(route='signup-redirect/',
         view=RedirectView.as_view(pattern_name='rest_register'),
         name='account_signup'),
    # Social auth
    path(route='github/', view=GithubLoginView.as_view(), name='github_login'),
    path(route='github/redirect/', view=github_views.oauth2_login,
         name='github_login_redirect'),
    path(route='github/callback/', view=github_callback, name='github_callback'),
    path(route='github/connect/', view=GithubConnectView.as_view(),
         name='github_connect'),
    path(route='google/', view=GoogleLoginView.as_view(), name='google_login'),
    path(route='google/redirect/', view=google_views.oauth2_login,
         name='google_login_redirect'),
    path(route='google/callback/', view=google_callback, name='google_callback'),
    path(route='google/connect/', view=GoogleConnectView.as_view(),
         name='google_connect'),
    path(route='socialaccounts/', view=SocialAccountListView.as_view(),
         name='socialaccount_connections'),
    path(route='socialaccounts/<int:pk>/disconnect/',
         view=SocialAccountDisconnectView.as_view(),
         name='socialaccount_disconnect')
]
