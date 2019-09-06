from datetime import datetime

class Rental:
    def __init__(self, id, start_date, end_date, distance, car_id):
        self.id = id
        self.distance = distance
        self.car_id = car_id

        # we add 1 because the first day is also billed
        self.duration = datetime.strptime(end_date, '%Y-%m-%d') - datetime.strptime(start_date, '%Y-%m-%d')
        self.duration = 1 + self.duration.days
        
    def compute_price(self, cars):
        "compute the price of a rental given the list of cards"
        car = cars[self.car_id]
        
        self.price = car.price_per_km * self.distance + car.price_per_day * self.duration

    def format_for_export(self):
        toreturn = {}
        toreturn["id"] = self.id
        toreturn["price"] = self.price
        return toreturn
