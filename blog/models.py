from datetime import date

from django.db import models
from django.urls import reverse
from django_stubs_ext.db.models import TypedModelMeta
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

    def __str__(self) -> str:
        return self.title

    class Meta(TypedModelMeta):
        ordering = ("-date",)
