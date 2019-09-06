import json
from checkout import Checkout
from data_from_db import DataFromDB


def start(path):
    # initializing data
    cars = {}
    rentals = []

    data = DataFromDB(path)
    cars = data.cars
    options = data.options

    for id, rental in data.rentals.items():
        try:
            checkout = Checkout(cars[rental.car_id], rental, options[id])
        except:
            # Values entered for checkout are incorrect -> we don't deal with this checkout
            pass
        else:
            rentals.append(checkout.format_for_export())

    with open('data/output.json', 'w', encoding='utf-8') as file:
        to_dump = {"rentals": rentals}
        json.dump(to_dump, file, ensure_ascii=False, indent=2)

start('data/input.json')
