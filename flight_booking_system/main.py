import random
import streamlit as st
from services.booking_service import book_flight, cancel_booking
from services.flight_service import add_flight
from models.booking import bookings
from models.flight import flights

def random_booking_id():
    while True:
        random_id = random.randint(10000,99999)
        if not random_id in bookings:
            return random_id

def main():
    global next_booking_id
    st.title("Flight Booking System")

    with st.form("Create flight"):
        st.title("Create flight")
        flight_number = st.text_input("Flight number")
        origin = st.text_input("Origin")
        destination = st.text_input("Destination")
        departure_time = st.text_input("Departure time")
        capacity = st.text_input("Capacity")
        if st.form_submit_button("Create flight"):
            try:
                add_flight(flight_number, origin, destination, departure_time, int(capacity))
                st.success("Succesfully created flight")
            except Exception as e:
                st.error(e)

    with st.form("Create booking"):
        st.title("Create booking")
        flight_number = st.selectbox("Flight number", list(flights.keys()))
        name = st.text_input("Name")
        if st.form_submit_button("Book flight") and flight_number != None:
            try:
                book_flight(f"{random_booking_id()}", flight_number, name)
                st.success("Succesfully booked flight")
            except Exception as e:
                st.error(e)
    
    bookings_to_cancel = []

    for booking in bookings.values():
        with st.expander(f"Booking {booking.booking_id}"):
            flight = flights[booking.flight_number]
            st.write(f"Flight {flight.flight_number} from {flight.origin} to {flight.destination}")
            st.write(f"Departs at {flight.departure_time}")
            st.write(f"Booked by {booking.passenger_name}")
            if st.button("Cancel booking", key=booking.booking_id):
                bookings_to_cancel.append(booking)

    for booking in bookings_to_cancel:
        try:
            cancel_booking(booking.booking_id)
            st.success(f"Succesfully cancelled booking {booking.booking_id}")
        except Exception as e:
            st.error(e)

if __name__ == "__main__":
    main()
