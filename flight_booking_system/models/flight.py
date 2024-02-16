from exceptions.custom_exceptions import FlightFullException


class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.capacity = capacity
        self.bookings = 0

    def available_seats(self):
        return self.capacity - self.bookings

    def add_booking(self):
        if not self.can_add_booking():
            raise FlightFullException(self.flight_number)
        self.bookings += 1

    def remove_booking(self):
        self.bookings -= 1

    def can_add_booking(self):
        return self.available_seats() > 0

flights: dict[str, Flight] = {}
