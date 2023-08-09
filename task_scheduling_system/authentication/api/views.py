import urllib

from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView, SocialConnectView, \
    RegisterView
from dj_rest_auth.serializers import TokenSerializer
from dj_rest_auth.views import LoginView, UserDetailsView
from django.shortcuts import redirect
from drf_spectacular.utils import extend_schema


@extend_schema(responses=TokenSerializer)
class CustomUserLoginView(LoginView):
    """
    Check the credentials and return the REST Token
    if the credentials are valid and authenticated.
    Calls Django Auth login method to register User ID
    in Django session framework.

    Accept the following POST parameters: email, password

    Return the REST Framework Token Object's key.
    """


class CustomUserDetailsView(UserDetailsView):
    """
    Reads and updates UserModel fields
    Accepts GET, PUT, PATCH methods.

    Default accepted fields: username, full_name

    Default display fields: pk, username, email, full_name

    Read-only fields: pk, email

    Returns UserModel fields.
    """


@extend_schema(responses=TokenSerializer)
class CustomUserRegisterView(RegisterView):
    """
    Create a new system account with credentials provided by the user.

    Accepts username, email, password and retyped password.

    Returns the REST Framework Token Object's key.
    """


@extend_schema(responses=TokenSerializer)
class GithubLoginView(SocialLoginView):
    """
    Receive code from user, send code to Github in exchange for an access token. Send
    access token to Github to retrieve Github account email for use in authentication
    or account registration.
    """
    adapter_class = GitHubOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/api/v1/auth/github/callback/'
    client_class = OAuth2Client


def github_callback(request):
    """
    Callback url defined in Github app console. Retrieve code from Github and
    redirect user back to the login page, with the code as a parameter on URL.
    """
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'http://127.0.0.1:8000/api/v1/auth/github?{params}')


class GithubConnectView(SocialConnectView):
    """
    Functions similar to GithubLoginView, but will link a Github account to an
    existing system account instead of creating a new account.
    """
    adapter_class = GitHubOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/api/v1/auth/github/callback/'
    client_class = OAuth2Client


@extend_schema(responses=TokenSerializer)
class GoogleLoginView(SocialLoginView):
    """
    Receive code from user, send code to Google in exchange for an access token. Send
    access token to Google to retrieve Google account email for use in authentication
    or account registration.
    """
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/api/v1/auth/google/callback/'
    client_class = OAuth2Client


def google_callback(request):
    """
    Callback url defined in Google app console. Retrieve code from Google and
    redirect user back to the login page, with the code as a parameter on URL.
    """
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'http://127.0.0.1:8000/api/v1/auth/google?{params}')


class GoogleConnectView(SocialConnectView):
    """
    Functions similar to GoogleLoginView, but will link a Google account to an
    existing system account instead of creating a new account.
    """
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/api/v1/auth/google/callback/'
    client_class = OAuth2Client
