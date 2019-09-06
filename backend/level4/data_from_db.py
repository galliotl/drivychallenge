import json

from models.car import Car
from models.rental import Rental


class DataFromDB:
    "get data from the file and format it to a more usable data structure"

    def __init__(self, path):
        # we get the data from the db, here the input file
        data_from_file = {}

        # init
        self.rentals = {}
        self.cars = {}

        try:
            with open(path) as f:
                data_from_file = json.load(f)
        except:
            raise IOError('Cannot open file, wrong path')
        else:
            if not ("rentals" or "cars") in data_from_file:
                "we need rentals and car at least to function properly"
                raise ValueError('File doesn\'t have the correct elements')

            # cars init
            for car in data_from_file["cars"]:
                try:
                    new_car = Car(car["id"], car["price_per_km"], car["price_per_day"])
                except:
                    print('Values entered for car are incorrect.', car["id"])
                else:
                    self.cars[car["id"]] = new_car
            
            # rentals
            for rental in data_from_file["rentals"]:
                try:
                    new_rental = Rental(rental["id"], rental["start_date"], rental["end_date"], rental["distance"], rental["car_id"])
                except:
                    print('Values entered for rental are incorrect.', rental["id"])
                else:
                    # we check if the car exists before adding the rental
                    if new_rental.car_id in self.cars:
                        self.rentals[new_rental.id] = new_rental