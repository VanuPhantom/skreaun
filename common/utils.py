from typing import Protocol

from django.test import TestCase
from pyquery import PyQuery


class ResponseWithContent(Protocol):
    content: bytes = b""


class HtmxTestCase(TestCase):
    def assertIsPartial(self, response: ResponseWithContent):
        self.assertFalse(PyQuery(response.content).is_("html"))

    def assertIsNotPartial(self, response: ResponseWithContent):
        self.assertTrue(PyQuery(response.content).is_("html"))
