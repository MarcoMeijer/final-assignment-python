
class FlightFullException(Exception):
    def __init__(self, flight_number):            
        super().__init__(f"Flight {flight_number} is already full")
        self.flight_number = flight_number

class BookingNotFoundException(Exception):
    def __init__(self, booking_id):            
        super().__init__(f"Booking with id {booking_id} is not found")
        self.booking_id = booking_id

class BookingAlreadyExistsException(Exception):
    def __init__(self, booking_id):            
        super().__init__(f"Booking with id {booking_id} already exists")
        self.booking_id = booking_id

class FlightAlreadyExistsException(Exception):
    def __init__(self, flight_number):            
        super().__init__(f"Flight {flight_number} already exists")
        self.flight_number = flight_number

class FlightNotFoundException(Exception):
    def __init__(self, flight_number):            
        super().__init__(f"Flight {flight_number} not found")
        self.flight_number = flight_number

