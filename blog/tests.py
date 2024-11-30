from datetime import date
from typing import cast

from django.test import TestCase
from django.urls import reverse
from pyquery import PyQuery

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


class PostViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.bulk_create(
            [Post(title=f"Post {n}", content="Nyaaa *paws* :3") for n in range(100)]
        )

    def test_existing_post_gives_200(self):
        post = cast(Post, Post.objects.first())

        response = self.client.get(reverse("blog:post", args=[post.pk]))

        self.assertEqual(response.status_code, 200)

    def test_non_existent_post_gives_404(self):
        response = self.client.get(reverse("blog:post", args=[300]))

        self.assertEqual(response.status_code, 404)

    def test_htmx_headers_give_partial(self):
        post = cast(Post, Post.objects.first())

        response = self.client.get(
            reverse("blog:post", args=[post.pk]), headers={"HX-Request": "true"}
        )

        self.assertFalse(PyQuery(response.content).is_("html"))

    def test_no_htmx_headers_give_full(self):
        post = cast(Post, Post.objects.first())

        response = self.client.get(reverse("blog:post", args=[post.pk]))

        self.assertTrue(PyQuery(response.content).is_("html"))
