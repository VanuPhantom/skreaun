from datetime import date
from typing import cast

from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlencode

from common.utils import HtmxTestCase

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


class TestCaseWithPosts(HtmxTestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.bulk_create(
            [Post(title=f"Post {n}", content="Nyaaa *paws* :3") for n in range(100)]
        )


class PostViewTests(TestCaseWithPosts):
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

        self.assertIsPartial(response)

    def test_no_htmx_headers_give_full(self):
        post = cast(Post, Post.objects.first())

        response = self.client.get(reverse("blog:post", args=[post.pk]))

        self.assertIsNotPartial(response)


class PostListViewTests(TestCaseWithPosts):
    def test_responds_with_ok(self):
        response = self.client.get(reverse("blog:index"))

        self.assertEqual(response.status_code, 200)

    def test_handles_invalid_page_numbers(self):
        response = self.client.get(
            f"%s?%s"
            % (reverse("blog:index"), urlencode({"page": "lorem ipsum dolor sit amet"}))
        )

        self.assertEqual(response.status_code, 200)

    def test_htmx_headers_give_partial(self):
        response = self.client.get(
            reverse("blog:index"), headers={"HX-Request": "true"}
        )

        self.assertIsPartial(response)

    def test_no_htmx_headers_give_full(self):
        response = self.client.get(reverse("blog:index"))

        self.assertIsNotPartial(response)
