import pytest
from classes.many_to_many import NationalPark, Visitor, Trip

class TestVisitor:

    def test_name_is_mutable_string(self):
        visitor = Visitor("Bob")
        assert isinstance(visitor.name, str)
        visitor.name = 2
        assert visitor.name == "Bob"

    def test_name_has_valid_length(self):
        vis = Visitor("Poppy")
        vis.name = "TooLongTobeValid"
        assert vis.name == "Poppy"

    def test_has_many_trips(self):
        p1 = NationalPark("Yosemite")
        vis = Visitor("Bill")
        vis2 = Visitor("Steve")
        Trip(vis, p1, "May 5th", "May 9th")
        Trip(vis, p1, "May 20th", "May 27th")
        Trip(vis2, p1, "January 5th", "January 20th")
        assert len(vis.trips()) == 2

    def test_trips_of_type_trips(self):
        vis = Visitor("Phil")
        p1 = NationalPark("Yellow Stone")
        Trip(vis, p1, "May 5th", "May 9th")
        Trip(vis, p1, "May 20th", "May 27th")
        assert isinstance(vis.trips()[0], Trip)

    def test_has_many_parks(self):
        vis_1 = Visitor("Flat White")
        vis_2 = Visitor("Steve")
        p1 = NationalPark("Alaska Wilds")
        p2 = NationalPark("Bryce Canyon")
        Trip(vis_1, p1, "May 5th", "May 9th")
        Trip(vis_1, p2, "May 20th", "May 27th")
        Trip(vis_2, p2, "August 20th", "August 27th")
        assert len(vis_1.national_parks()) == 2

    def test_has_unique_parks(self):
        p1 = NationalPark("Yosemite")
        p2 = NationalPark("Rocky Mountain")
        vis = Visitor("Steeve")
        Trip(vis, p1, "May 5th", "May 9th")
        Trip(vis, p1, "May 20th", "May 27th")
        Trip(vis, p2, "January 5th", "January 20th")
        assert len(set(vis.national_parks())) == len(vis.national_parks())

    def test_parks_of_type_park(self):
        p1 = NationalPark("Yosemite")
        p2 = NationalPark("Rocky Mountain")
        vis = Visitor("Steeeve")
        Trip(vis, p1, "May 5th", "May 9th")
        Trip(vis, p2, "January 5th", "January 20th")
        assert isinstance(vis.national_parks()[0], NationalPark)
