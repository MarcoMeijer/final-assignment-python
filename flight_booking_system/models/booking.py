class Booking:
    def __init__(self, booking_id: str, flight_number: str, passenger_name: str):
        self.booking_id = booking_id
        self.flight_number = flight_number
        self.passenger_name = passenger_name

bookings: dict[str, Booking] = {}
