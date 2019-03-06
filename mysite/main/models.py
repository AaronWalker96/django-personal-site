from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
