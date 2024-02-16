from exceptions.custom_exceptions import BookingAlreadyExistsException, BookingNotFoundException, FlightNotFoundException
from services.flight_service import update_flight
from models.booking import Booking, bookings
from models.flight import flights

def book_flight(booking_id: str, flight_number: str, passenger_name: str):
    booking = Booking(booking_id, flight_number, passenger_name)
    if booking_id in bookings:
        raise BookingAlreadyExistsException(booking_id)
    update_flight(flight_number)
    bookings[booking_id] = booking

def cancel_booking(booking_id: str):
    if not booking_id in bookings:
        raise BookingNotFoundException(booking_id)
    booking = bookings[booking_id]
    flight_number = booking.flight_number
    if not flight_number in flights:
        raise FlightNotFoundException(flight_number)
    flight = flights[flight_number]
    flight.remove_booking()
    del bookings[booking_id]

