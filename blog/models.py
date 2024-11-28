from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    @property
    def url(self):
        return reverse("post", args=[self.id]) # type: ignore

