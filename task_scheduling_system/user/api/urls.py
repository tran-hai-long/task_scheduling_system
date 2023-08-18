from dj_rest_auth.views import UserDetailsView
from django.urls import path

from task_scheduling_system.user.api.views import CustomPasswordChangeView

urlpatterns = [
    path(route='profile/', view=UserDetailsView.as_view(),
         name='rest_user_details'),
    path(route='change-password/', view=CustomPasswordChangeView.as_view(),
         name='rest_password_change'),
]
