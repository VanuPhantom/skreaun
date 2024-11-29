from datetime import date

from django.db import models
from django.urls import reverse
from markdown import markdown

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField(default=date.today)

    @property
    def url(self):
        return reverse("blog:post", args=[self.pk])

    @property
    def html(self):
        return markdown(self.content)
