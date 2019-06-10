from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()
    author = models.TextField(blank=True)

    def __str__(self):
        return self.text[:50]