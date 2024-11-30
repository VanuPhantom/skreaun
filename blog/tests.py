from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostTests(TestCase):
    def test_stringify_returns_title(self):
        post = Post(title="Test", content="Hello, world")
        self.assertEqual(post.title, str(post))

    def test_default_data_is_today(self):
        post = Post(title="Test", content="Hello, world")
        self.assertEqual(post.date, date.today())

    def test_url_points_to_post(self):
        post = Post(title="Test", content="Hello, world")
        post.save()

        url = reverse("blog:post", args=[post.pk])

        self.assertEqual(post.url, url)
