from dj_rest_auth.views import PasswordChangeView
from drf_spectacular.utils import extend_schema

from task_scheduling_system.authentication.api.serializers import DetailSerializer


@extend_schema(responses=DetailSerializer)
class CustomPasswordChangeView(PasswordChangeView):
    """Enter old password and new password. Return success/fail message."""
