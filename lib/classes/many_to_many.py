# lib/classes/many_to_many.py

class NationalPark:
    all_parks = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters.")
        self._name = name
        NationalPark.all_parks.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Name is immutable
        pass

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return list(set(trip.visitor for trip in self.trips()))

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        visitor_count = {}
        for trip in self.trips():
            visitor_count[trip.visitor] = visitor_count.get(trip.visitor, 0) + 1
        if not visitor_count:
            return None
        return max(visitor_count, key=visitor_count.get)


class Visitor:
    all_visitors = []

    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = name
        Visitor.all_visitors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        # else do nothing (immutable if invalid)

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        return list(set(trip.national_park for trip in self.trips()))


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(visitor, Visitor):
            raise TypeError("visitor must be a Visitor object.")
        if not isinstance(national_park, NationalPark):
            raise TypeError("national_park must be a NationalPark object.")
        if not isinstance(start_date, str) or len(start_date) < 3:
            raise ValueError("start_date must be a string with valid length.")
        if not isinstance(end_date, str) or len(end_date) < 3:
            raise ValueError("end_date must be a string with valid length.")

        self.visitor = visitor
        self.national_park = national_park
        self._start_date = start_date
        self._end_date = end_date

        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._end_date = value
