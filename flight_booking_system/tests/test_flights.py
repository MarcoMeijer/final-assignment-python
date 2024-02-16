import unittest
from exceptions.custom_exceptions import FlightAlreadyExistsException
from services.flight_service import add_flight, update_flight
from models.flight import flights

class TestFlightServices(unittest.TestCase):
    def tearDown(self) -> None:
        flights.clear()

    def test_add_flight(self):
        self.assertNotIn("FN235", flights)
        add_flight(flight_number="FN235", origin="Barcelona", destination="Madrid", capacity=60, departure_time="11:30")
        self.assertIn("FN235", flights)

        flight = flights["FN235"]
        self.assertEqual(flight.flight_number, "FN235")
        self.assertEqual(flight.origin, "Barcelona")
        self.assertEqual(flight.destination, "Madrid")
        self.assertEqual(flight.capacity, 60)
        self.assertEqual(flight.departure_time, "11:30")

        self.assertRaises(FlightAlreadyExistsException, add_flight, "FN235", "Barcelona", "Madrid", 60, "11:30")

    def test_update_flight(self):
        add_flight(flight_number="FN235", origin="Barcelona", destination="Madrid", capacity=60, departure_time="11:30")
        self.assertIn("FN235", flights)

        flight = flights["FN235"]
        self.assertEqual(flight.available_seats(), 60)
        update_flight("FN235")
        self.assertEqual(flight.available_seats(), 59)
