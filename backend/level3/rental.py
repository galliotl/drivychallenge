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

    def compute_commission(self):
        commission = {}
        commission_rate = 0.3
        insurance_rate = 0.5
        commission["insurance_fee"] = int(self.price * commission_rate * insurance_rate)
        # we multiply by 100 because the price is an int in cents
        commission["assistance_fee"] = int(self.duration * 100)
        commission["drivy_fee"] = int(self.price * commission_rate - commission["insurance_fee"] - commission["assistance_fee"])
        self.commission = commission

    def format_for_export(self):
        toreturn = {}
        toreturn["id"] = self.id
        if self.price:
            toreturn["price"] = self.price
        if self.commission:
            toreturn["commission"] = self.commission
        return toreturn
