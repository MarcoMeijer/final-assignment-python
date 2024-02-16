import unittest
from exceptions.custom_exceptions import FlightFullException
from services.booking_service import book_flight, cancel_booking
from services.flight_service import add_flight, update_flight
from models.flight import flights
from models.booking import bookings

class TestBookingsService(unittest.TestCase):
    def setUp(self) -> None:
        add_flight(flight_number="FN235", origin="Barcelona", destination="Madrid", capacity=60, departure_time="11:30")
        self.assertIn("FN235", flights)

        self.flight = flights["FN235"]
    
    def tearDown(self) -> None:
        flights.clear()
        bookings.clear()

    def test_book_flight(self):
        self.assertEqual(self.flight.available_seats(), 60)
        
        book_flight(flight_number="FN235", booking_id="abc123", passenger_name="Marco Meijer")

        self.assertEqual(self.flight.available_seats(), 59)
        self.assertIn("abc123", bookings)

        booking = bookings["abc123"]
        self.assertEqual(booking.flight_number, "FN235")
        self.assertEqual(booking.booking_id, "abc123")
        self.assertEqual(booking.passenger_name, "Marco Meijer")

    def test_booking_full(self):
        self.assertEqual(self.flight.available_seats(), 60)
        
        for i in range(60):
            book_flight(flight_number="FN235", booking_id=f"abc{i}", passenger_name="Marco Meijer")

        self.assertEqual(self.flight.available_seats(), 0)

        self.assertRaises(FlightFullException, book_flight, flight_number="FN235", booking_id="abc123", passenger_name="Marco Meijer")
        self.assertEqual(self.flight.available_seats(), 0)

        cancel_booking("abc0")

        self.assertEqual(self.flight.available_seats(), 1)

        book_flight(flight_number="FN235", booking_id="abc123", passenger_name="Marco Meijer")

        self.assertEqual(self.flight.available_seats(), 0)

    def test_cancel_booking(self):
        self.assertEqual(self.flight.available_seats(), 60)

        book_flight(flight_number="FN235", booking_id="abc123", passenger_name="Marco Meijer")

        self.assertEqual(self.flight.available_seats(), 59)
        self.assertIn("abc123", bookings)

        cancel_booking("abc123")
        self.assertEqual(self.flight.available_seats(), 60)

        self.assertNotIn("abc123", bookings)


