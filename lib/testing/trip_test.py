import pytest
from classes.many_to_many import NationalPark, Visitor, Trip

class TestTrip:

    def setup_method(self):
        Trip.all = []

    def test_start_date_is_mutable_string(self):
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")
        assert isinstance(trip.start_date, str)
        trip.start_date = "May 6th"
        assert trip.start_date == "May 6th"
        trip.start_date = 2
        assert trip.start_date == "May 6th"

    def test_start_date_has_valid_length(self):
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")
        trip.start_date = "Ma"  # invalid
        assert trip.start_date == "May 5th"

    def test_end_date_is_mutable_string(self):
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")
        assert isinstance(trip.end_date, str)
        trip.end_date = "May 10th"
        assert trip.end_date == "May 10th"
        trip.end_date = 2
        assert trip.end_date == "May 10th"

    def test_end_date_has_valid_length(self):
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")
        trip.end_date = "Ma"  # invalid
        assert trip.end_date == "May 9th"

    def test_get_all_trips(self):
        Trip.all = []
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        john = Visitor("John")
        Trip(matteo, yosemite, "May 5th", "May 9th")
        Trip(john, yosemite, "May 20th", "May 27th")
        assert len(Trip.all) == 2
