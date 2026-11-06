coaches = {
    "SL": 10,
    "3A": 6,
    "2A": 4
}

berths = [
    "Lower",
    "Middle",
    "Upper",
    "Side Lower",
    "Side Upper"
]

seat_counter = 1


def allocate_seat():

    global seat_counter

    seat_number = seat_counter

    berth_type = berths[(seat_counter - 1) % 5]

    coach_number = (seat_counter - 1) // 72 + 1

    seat_counter += 1

    return coach_number, seat_number, berth_type