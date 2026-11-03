from django.test import TestCase,SimpleTestCase
from accounts.views import add

# Create your tests here.
class AddFunctionTestCase(SimpleTestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)