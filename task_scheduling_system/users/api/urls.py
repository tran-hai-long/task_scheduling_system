from allauth.socialaccount.providers.github.views import oauth2_login
from django.urls import path

from ..api.views import CustomUserListAPIView, CustomUserRetrieveUpdateDestroyAPIView, \
    GithubLoginView, github_callback

urlpatterns = [
    path(route='users/', view=CustomUserListAPIView.as_view(),
         name='custom_user_list_api'),
    path(route='user/<int:pk>', view=CustomUserRetrieveUpdateDestroyAPIView.as_view(),
         name='custom_user_retrieve_update_destroy_api'),
    path(route='auth/github/', view=GithubLoginView.as_view(), name='github_login'),
    path(route='auth/github/url/', view=oauth2_login, name='github_login_redirect'),
    path(route='auth/github/callback/', view=github_callback, name='github_callback'),
]
