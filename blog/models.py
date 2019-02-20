from django.conf import settings
from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='Cowboy Bebop: Ultimate Anime Analysis')
    desc = models.TextField(max_length=200, default='A simple description will suffice')
    body = MarkdownxField(default='This is where the content of the post will go')
    link = models.TextField(default='For example: https://www.roblox.com/NewLogin')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    @property
    def formatted_markdown(self):
        return markdownify(self.body)

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return self.title
