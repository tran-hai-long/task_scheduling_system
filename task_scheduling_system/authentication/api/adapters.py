from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.sites.shortcuts import get_current_site

from task_scheduling_system.settings import FRONTEND_CONFIRM_EMAIL_URL


class CustomEmailAdapter(DefaultAccountAdapter):

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        current_site = get_current_site(request)
        activate_url = FRONTEND_CONFIRM_EMAIL_URL
        ctx = {
            "user": emailconfirmation.email_address.user,
            "activate_url": activate_url,
            "current_site": current_site,
            "key": emailconfirmation.key,
        }
        if signup:
            email_template = "authentication/api/email_confirmation_signup"
        else:
            email_template = "authentication/api/email_confirmation"
        self.send_mail(email_template, emailconfirmation.email_address.email, ctx)
