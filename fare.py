def calculate_fare(distance, coach):

    rates = {
        "SL": 1.5,
        "3A": 3.0,
        "2A": 4.5
    }

    if coach not in rates:
        return 0

    fare = distance * rates[coach]

    return round(fare, 2)