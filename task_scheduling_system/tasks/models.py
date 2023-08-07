from django.core.exceptions import ValidationError
from django.db import models

from ..authentication.models import CustomUser


# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        (0, "Chua lam"),
        (1, "Dang lam"),
        (2, "Da xong")
    ]
    PRIORITY_CHOICES = [
        (0, "Thap"),
        (1, "Trung binh"),
        (2, "Cao")
    ]

    name = models.CharField(max_length=99)
    description = models.TextField(max_length=999, blank=True, null=False)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    planned_time = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=0)
    priority = models.SmallIntegerField(choices=PRIORITY_CHOICES, default=1)
    to_do = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def clean(self):
        if self.description is None:
            self.description = ""
        if self.start_time is not None and self.end_time is not None and self.end_time < self.start_time:
            raise ValidationError("End time must be later than start time.")
        if self.planned_time is not None and self.start_time is not None and self.planned_time < self.start_time:
            raise ValidationError("Planned time must be later than start time.")
        if self.planned_time is not None and self.end_time is not None and self.planned_time > self.end_time:
            raise ValidationError("Planned time must be sooner than end time.")

    def __str__(self):
        return self.name
