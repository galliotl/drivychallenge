import datetime

class Rental:
    def __init__(self, id, start_date, end_date, distance, car_id):
        self.id = id
        self.distance = distance
        self.car_id = car_id
        # we add 1 because the first day is also billed
        self.duration = datetime.datetime.strptime(end_date, '%Y-%m-%d') - datetime.datetime.strptime(start_date, '%Y-%m-%d')
        self.duration = 1 + self.duration.days

    def compute_price(self, cars):
        "compute the price of a rental given the list of cards and decreases using the given params"
        car = cars[self.car_id]

        # we init the price with the distance
        self.price = car.price_per_km * self.distance

        # we apply the decay
        for x in range(0, self.duration):
            if x < 1:
                self.price += car.price_per_day
            elif x < 4:
                self.price += car.price_per_day * 0.9
            elif x < 10:
                self.price += car.price_per_day * 0.7
            else:
                self.price += car.price_per_day * 0.5
        self.price = int(self.price)

    def format_for_export(self):
        toreturn = {}
        toreturn["id"] = self.id
        toreturn["price"] = self.price
        return toreturn
