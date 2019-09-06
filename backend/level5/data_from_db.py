import json

from models.car import Car
from models.rental import Rental
from models.options import Option


class DataFromDB:
    "get data from the file and format it to a more usable data structure"

    def __init__(self, path):
        # we get the data from the db, here the input file
        data_from_file = {}

        # init
        self.rentals = {}
        self.options = {}
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
                    # Values entered for car are incorrect -> we don't deal with this car
                    pass
                else:
                    self.cars[car["id"]] = new_car
            
            # rentals
            for rental in data_from_file["rentals"]:
                try:
                    new_rental = Rental(rental["id"], rental["start_date"], rental["end_date"], rental["distance"], rental["car_id"])
                except:
                    # Values entered for rental are incorrect -> we don't deal with this rental
                    pass
                else:
                    # we check if the car exists before adding the rental
                    if new_rental.car_id in self.cars:
                        self.rentals[new_rental.id] = new_rental

                        # we init the options to an empty array for each rental
                        self.options[new_rental.id] = []

            # options
            if data_from_file["options"]:
                for option_from_file in data_from_file["options"]:
                    try:
                        new_option = Option(option_from_file["id"], option_from_file["rental_id"], option_from_file["type"])
                    except:
                        # Values entered for options are incorrect -> we don't deal with this option
                        pass
                    else:
                        # we verify if the rental that the option is attached to exists
                        if new_option.rental_id in self.rentals:
                            self.options[new_option.rental_id].append(new_option)
