from unittest import TestCase
from Ex1 import Airline


class TestAirline(TestCase):
    def setUp(self):
        self.flight = Airline('AF 3535', 'Airbus', '12:40', 'MON, WED, FRI, SUN')

    def test_object_instance(self):
        self.assertIsInstance(self.flight, Airline)

    def test_get_destination(self):
        self.assertEqual(self.flight.description, 'Destination: ')

    def test_get_destination_static(self):
        self.assertEqual(self.flight.getDestinationStatic(), 'London')

    def test_setattr(self):
        self.assertIsNot(self.flight.__setattr__('New York', 'Moscow'), '')

