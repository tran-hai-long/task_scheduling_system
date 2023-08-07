from django.urls import path

from ..api.views import CustomUserListAPIView, CustomUserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path(route='users/', view=CustomUserListAPIView.as_view(),
         name='custom_user_list_api'),
    path(route='user/<int:pk>/', view=CustomUserRetrieveUpdateDestroyAPIView.as_view(),
         name='custom_user_retrieve_update_destroy_api'),
]
