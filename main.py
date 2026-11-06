from train import view_train_details
from booking import book_ticket, check_booking_status
from cancellation import cancel_ticket


while True:

    print("\n================================")
    print("     TRAIN RESERVATION SYSTEM")
    print("================================")

    print("1. View Train Details")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Check Booking Status")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        view_train_details()

    elif choice == "2":

        book_ticket()

    elif choice == "3":

        cancel_ticket()

    elif choice == "4":

        check_booking_status()

    elif choice == "5":

        print("Thank you for using Train Reservation System!")
        break

    else:

        print("Invalid Choice!")