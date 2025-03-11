from datetime import datetime
from typing import Optional

from django.contrib.auth import get_user_model
from django.db import models

from .schemas import PostSchema

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
