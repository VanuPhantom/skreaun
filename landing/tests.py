from django.urls import reverse

from common.utils import HtmxTestCase


# Create your tests here.
class LandingPageTests(HtmxTestCase):
    def test_htmx_headers_give_partial(self):
        response = self.client.get(
            reverse("landing:index"), headers={"HX-Request": "true"}
        )

        self.assertIsPartial(response)

    def test_no_htmx_headers_give_full(self):
        response = self.client.get(reverse("landing:index"))

        self.assertIsNotPartial(response)
