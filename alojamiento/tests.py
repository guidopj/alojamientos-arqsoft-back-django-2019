from django.test import TestCase
from .models import Alojamiento

class AlojamientoTests(TestCase):

  def setUp(self):
    Alojamiento.objects.create(
      state="State",
      town="Town",
      address="Address",
      type="Type",
      category="Category"
    )

  def test_empty_set_should_be_true(self):
    sut = Alojamiento.objects.get(state="State")
    self.assertEqual(sut.town, "Town")
    self.assertEqual(sut.address, "Address")
    self.assertEqual(sut.type, "Type")
    self.assertEqual(sut.category, "Category")
    self.assertEqual(sut.state, "State")
  