import json
import os

from train import stations, get_station_details
from allocation import allocate_seat
from fare import calculate_fare

FILE = "bookings.json"


def load_bookings():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}


bookings = load_bookings()


def save_bookings():
    with open(FILE, "w") as f:
        json.dump(bookings, f, indent=4)


def book_ticket():

    print("\n===== BOOK TICKET =====")

    passenger_count = int(input("Enter Number of Passengers (1-6): "))

    if passenger_count < 1 or passenger_count > 6:
        print("Invalid Passenger Count!")
        return

    source = int(input("Enter Source Station Number: "))
    destination = int(input("Enter Destination Station Number: "))

    distance = get_station_details(source, destination)

    if distance is None:
        print("Invalid Source or Destination!")
        return

    coach = input("Enter Coach (SL / 3A / 2A): ").upper()

    if coach not in ["SL", "3A", "2A"]:
        print("Invalid Coach!")
        return

    passengers = []

    for i in range(passenger_count):

        print("\nPassenger", i + 1)

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")

        coach_no, seat_no, berth = allocate_seat()

        fare = calculate_fare(distance, coach)

        passengers.append({
            "name": name,
            "age": age,
            "gender": gender,
            "coach": coach,
            "coach_number": coach_no,
            "seat_number": seat_no,
            "berth": berth,
            "status": "CONFIRMED",
            "fare": fare
        })

    booking_id = max([int(x) for x in bookings.keys()], default=1000) + 1

    bookings[str(booking_id)] = {
        "passengers": passengers,
        "source": stations[source][0],
        "destination": stations[destination][0],
        "distance": distance
    }

    save_bookings()

    print("\n===== BOOKING SUCCESSFUL =====")
    print("Booking ID:", booking_id)

    for passenger in passengers:
        print("Passenger:", passenger["name"])
        print("Coach:", passenger["coach"])
        print("Seat:", passenger["seat_number"])
        print("Berth:", passenger["berth"])
        print("Status:", passenger["status"])
        print("Fare: Rs.", passenger["fare"])


def check_booking_status():

    print("\n===== BOOKING STATUS =====")

    bid = input("Enter Booking ID: ")

    if bid not in bookings:
        print("No Booking Records Found!")
        return

    for passenger in bookings[bid]["passengers"]:
        print(
            passenger["name"],
            "|",
            passenger["status"],
            "| Seat:",
            passenger["seat_number"]
        )