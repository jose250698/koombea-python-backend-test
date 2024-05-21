from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    title = models.CharField(max_length=255)
    total_links = models.IntegerField(default=0)
    is_processing = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Link(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    url = models.URLField()
    name = models.TextField()

    def __str__(self):
        return self.url
