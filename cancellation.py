from booking import bookings, save_bookings


def cancel_ticket():

    print("\n===== CANCEL TICKET =====")

    bid = input("Enter Booking ID: ").strip()

    if bid not in bookings:
        print("No booking records found!")
        return

    passengers = bookings[bid]["passengers"]

    if all(p["status"] == "CANCELLED" for p in passengers):
        print("Ticket already cancelled!")
        return

    for passenger in passengers:
        passenger["status"] = "CANCELLED"

    save_bookings()

    print("Ticket cancelled successfully!")