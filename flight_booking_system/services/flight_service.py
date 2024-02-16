from exceptions.custom_exceptions import FlightAlreadyExistsException, FlightNotFoundException
from utils.validator import validate_flight_number
from models.flight import Flight, flights

def add_flight(flight_number: str, origin: str, destination: str, departure_time: str, capacity: int):
    validate_flight_number(flight_number)
    flight = Flight(flight_number, origin, destination, departure_time, capacity)
    if flight_number in flights:
        raise FlightAlreadyExistsException(flight_number)
    flights[flight_number] = flight

def update_flight(flight_number: str):
    if not flight_number in flights:
        raise FlightNotFoundException(flight_number)
    flight = flights[flight_number]
    flight.add_booking()
