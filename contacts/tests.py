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

    def test_basic_multiplication(self):
        """
        Tests that  5 * 2 always equals 10.
        """
        self.assertEqual(5 * 2, 10)

    def test_basic_division(self):
        """
        Tests that  10 / 2 always equals 5.
        """
        self.assertEqual(10 / 2, 5)

    def test_basic_power(self):
        """
        Tests that 2 ** 2 always equals 4.
        """
        self.assertEqual(2 ** 2, 4)

    def test_basic_reminder(self):
        """
        Tests that 5 % 2 always equals 1.
        """
        self.assertEqual(5 % 2, 1)

    def test_basic_string(self):
        self.assertEqual('sony', 'sony')

    def test_basic_integer(self):
        self.assertEqual(5, 5)
