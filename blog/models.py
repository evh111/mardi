from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='Cowboy Bebop: Ultimate Anime Analysis')
    desc = models.TextField(max_length=200, default='A simple description will suffice')
    body = models.TextField(default='This is where the content of the post will go')
    link = models.TextField(default='For example: https://www.roblox.com/NewLogin')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return self.title
