import unittest

from utils.validator import validate_flight_number

class TestValidations(unittest.TestCase):
    def test_correct_flight_number(self):
        validate_flight_number("FN235")

    def test_flight_number_incorrect_length(self):
        self.assertRaises(ValueError, validate_flight_number, "F")
        self.assertRaises(ValueError, validate_flight_number, "FN1")
        self.assertRaises(ValueError, validate_flight_number, "FN")
        self.assertRaises(ValueError, validate_flight_number, "FN43295")
        self.assertRaises(ValueError, validate_flight_number, "AAAAAA")

    def test_flight_number_incorrect_prefix(self):
        self.assertRaises(ValueError, validate_flight_number, "AB123")
