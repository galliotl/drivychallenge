import json
from car import Car
from rental import Rental


def start(path):
    # initializing data
    data_from_file = {}
    cars = {}
    rentals = []

    with open(path) as f:
        data_from_file = json.load(f)

    for car in data_from_file["cars"]:
        cars[car["id"]] = Car(
            car["id"], car["price_per_km"], car["price_per_day"])

    for rental in data_from_file["rentals"]:
        new_rental = Rental(rental["id"], rental["start_date"],
                            rental["end_date"], rental["distance"], rental["car_id"])
        new_rental.compute_price(cars)
        rentals.append(new_rental.format_for_export())

    with open('data/output.json', 'w', encoding='utf-8') as file:
        to_dump = {}
        to_dump["rentals"] = rentals
        json.dump(to_dump, file, ensure_ascii=False, indent=4)


start('data/input.json')
