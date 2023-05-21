from django.test import TestCase
from .views import *


class ExchangeTest(TestCase):
    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)




