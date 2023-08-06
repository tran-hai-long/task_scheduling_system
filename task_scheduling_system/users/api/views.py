import urllib.parse

from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.shortcuts import redirect
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import CustomUserSerializer
from ..models import CustomUser


class CustomUserListAPIView(ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()


class CustomUserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()


class GithubLoginView(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/api/v1/users/auth/github/callback/'
    client_class = OAuth2Client


def github_callback(request):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'http://127.0.0.1:8000/api/v1/users/auth/github?{params}')
