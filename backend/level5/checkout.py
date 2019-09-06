class Checkout:
    commission_rate = 0.3
    insurance_rate = 0.5

    def __init__(self, car, rental, options):
        self.rental = rental
        self.car = car
        self.options = options

        self.compute_price()
        self.compute_actions()

    def compute_price(self):
        "compute the price of a rental and decreases using the given params then sets the rental price"

        # we init the price with the distance
        price = self.car.price_per_km * self.rental.distance

        # we apply the decay
        for x in range(0, self.rental.duration):
            if x < 1:
                price += self.car.price_per_day
            elif x < 4:
                price += self.car.price_per_day * 0.9
            elif x < 10:
                price += self.car.price_per_day * 0.7
            else:
                price += self.car.price_per_day * 0.5
        price = int(price)

        self.price = price

    def compute_actions(self):
        "computes the share for each member"
        # price without option has to be defined first
        assert self.price        

        # share formulas
        insurance = int(self.price * self.commission_rate * self.insurance_rate)
        assistance = int(self.rental.duration * 100)
        drivy = int(self.price * self.commission_rate - insurance - assistance)
        owner = int(self.price * (1 - self.commission_rate))

        # init shares
        share = {
            "insurance_fee": insurance,
            "assistance_fee": assistance,
            "drivy_fee": drivy,
            "owner_share": owner
        }
        
        # we add the options fare to the global price and to the share of the target member
        for option in self.options:
            to_add = int(option.price_per_day * self.rental.duration)
            self.price += to_add
            share[option.who] += to_add
        
        self.actions = [
            # drivers's debit
            {
                "who": "driver",
                "type": "debit",
                "amount": self.price
            },
            # owner's credit
            {
                "who": "owner",
                "type": "credit",
                "amount": share["owner_share"]
            },
            # insurance's credit
            {
                "who": "insurance",
                "type": "credit",
                "amount": share["insurance_fee"]
            },
            # assistance's credit
            {
                "who": "assistance",
                "type": "credit",
                "amount": share["assistance_fee"]
            },
            # drivy's credit
            {
                "who": "drivy",
                "type": "credit",
                "amount": share["drivy_fee"]
            }
        ]
    
    def format_for_export(self):
        # we verify the presence of mandatory fields
        if not self.actions:
            return False

        # we only use the options type in the returned statement
        options = []
        for option in self.options:
            options.append(option.type)

        toreturn = {
            'id': self.rental.id,
            'options': options,
            'actions': self.actions,
        }

        return toreturn
