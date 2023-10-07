from django.db import models
from django.contrib.auth.models import User

class Bio(models.Model):
    """biography of users"""
    text=models.CharField(max_length=100)
    owner=models.ForeignKey(User,models.CASCADE)

    def __str__(self):
        return self.text

