train_number = 12678
train_name = "Karnataka Express"

stations = {
    1: ("Bengaluru", 0),
    2: ("Tumakuru", 70),
    3: ("Tiptur", 140),
    4: ("Arsikere", 180),
    5: ("Birur", 250),
    6: ("Davangere", 350),
    7: ("Hubballi", 450),
    8: ("Belagavi", 550),
    9: ("Miraj", 650),
    10: ("Pune", 800),
    11: ("Bhopal", 1200),
    12: ("Delhi", 1800)
}


def view_train_details():

    print("\n===== TRAIN DETAILS =====")
    print("Train Number:", train_number)
    print("Train Name:", train_name)

    for number, details in stations.items():
        print(number, details[0], "-", details[1], "KM")


def get_station_details(source, destination):

    if source not in stations or destination not in stations:
        return None

    if source == destination:
        return None

    distance = abs(stations[destination][1] - stations[source][1])

    return distance