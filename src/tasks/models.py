from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)  # when model was created
    updated = models.DateTimeField(auto_now=True)  # everytime the model is saved

    class Meta:
        permissions = (
            ('view_task', 'Can view tasks'),
        )
