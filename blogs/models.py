from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """user's posts """
    title=models.CharField(max_length=20)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,models.CASCADE)

    def __str__(self):
        """string representation of the blog's post"""
        return self.text[:50]+"..."

