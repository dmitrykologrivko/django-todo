from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)  # when model was created
    updated = models.DateTimeField(auto_now=True)  # everytime the model is saved

    def __str__(self):
        return self.text

    def is_owner(self, request):
        if self.user == request.user:
            return True
        return False
