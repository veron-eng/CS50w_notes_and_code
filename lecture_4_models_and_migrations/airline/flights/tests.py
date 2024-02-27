from django.test import TestCase, Client

# Create your tests here.

from .models import Flights, Airport, Passenger
from django.db.models import Max

class FlightTestCase(TestCase):

    def setUp(self):

        # Create airports.
        a1 = Airport.objects.create(code="AAA", city="City A")
        a2 = Airport.objects.create(code="BBB", city="City B")

        # Create flights.
        Flights.objects.create(origin=a1, destination=a2, duration=100)
        Flights.objects.create(origin=a1, destination=a1, duration=200)
        Flights.objects.create(origin=a1, destination=a2, duration=-100)


    def test_departures_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(), 3)

    def test_arrivals_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(), 1)

    def test_valid_flight(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f = Flights.objects.get(origin=a1, destination=a2, duration=100)
        self.assertTrue(f.is_valid_flight())

    def test_invalid_flight_destination(self):
        a1 = Airport.objects.get(code="AAA")
        f = Flights.objects.get(origin=a1, destination=a1)
        self.assertFalse(f.is_valid_flight())

    def test_invalid_flight_duration(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f = Flights.objects.get(origin=a1, destination=a2, duration=-100)
        self.assertFalse(f.is_valid_flight())

    def test_index(self):

    # Set up client to make requests
        c = Client()

    # Send get request to index page and store response
        response = c.get("/flights/")

    # Make sure status code is 200
        self.assertEqual(response.status_code, 200)

    # Make sure three flights are returned in the context
        self.assertEqual(response.context["flights"].count(), 3)


    def test_valid_flight_page(self):
        a1 = Airport.objects.get(code="AAA")
        f = Flights.objects.get(origin=a1, destination=a1)

        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code, 200)

    def test_invalid_flight_page(self):
        max_id = Flights.objects.all().aggregate(Max("id"))["id__max"]

        c = Client()
        response = c.get(f"/flights/{max_id + 1}")
        self.assertEqual(response.status_code, 404)

    def test_flight_page_passengers(self):
        f = Flights.objects.get(pk=1)
        p = Passenger.objects.create(first="Alice", last="Adams")
        f.passengers.add(p)

        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["passengers"].count(), 1)

    def test_flight_page_non_passengers(self):
        f = Flights.objects.get(pk=1)
        p = Passenger.objects.create(first="Alice", last="Adams")

        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["non_passengers"].count(), 1)