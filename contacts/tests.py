from django.test import TestCase

# Create your tests here.
from contacts.models import Contacts

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_basic_subtraction(self):
        """
        Tests that 1 - 1 always equals 0.
        """
        self.assertEqual(1 - 1, 0)
