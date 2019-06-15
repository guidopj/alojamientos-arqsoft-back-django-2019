from django.test import TestCase

class AnimalTestCase(TestCase):

    def setUp(self):
      pass

    def test_empty_set_should_be_true(self):
        """test_empty_set_should_be_true"""
        self.assertEqual(True, True)