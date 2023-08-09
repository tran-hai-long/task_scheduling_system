from allauth.socialaccount.providers.github import views as github_views
from allauth.socialaccount.providers.google import views as google_views
from dj_rest_auth.registration.views import SocialAccountListView, \
    SocialAccountDisconnectView, VerifyEmailView, ResendEmailVerificationView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView, LogoutView, \
    PasswordChangeView
from django.urls import path

from .views import CustomUserLoginView, CustomUserDetailsView, CustomUserRegisterView
from ..api.views import GithubLoginView, github_callback, GithubConnectView, \
    GoogleLoginView, google_callback, GoogleConnectView

urlpatterns = [
    # dj_rest_auth urls
    path(route='login/', view=CustomUserLoginView.as_view(), name='rest_login'),
    path(route='logout/', view=LogoutView.as_view(), name='rest_logout'),
    path(route='user/', view=CustomUserDetailsView.as_view(), name='rest_user_details'),
    path(route='password/change/', view=PasswordChangeView.as_view(),
         name='rest_password_change'),
    path(route='password/reset/', view=PasswordResetView.as_view(),
         name='rest_password_reset'),
    path(route='password/reset/confirm/', view=PasswordResetConfirmView.as_view(),
         name='rest_password_reset_confirm'),
    path(route='registration/', view=CustomUserRegisterView.as_view(),
         name='rest_register'),
    path(route='account-confirm-email/', view=VerifyEmailView.as_view(),
         name='account_email_verification_sent'),
    path(route='registration/resend-email/', view=ResendEmailVerificationView.as_view(),
         name="rest_resend_email"),
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
