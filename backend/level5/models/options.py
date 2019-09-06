class Option:
    def __init__(self, id, rental_id, type):
        self.id = id
        self.rental_id = rental_id
        self.type = type

        if type == "gps":
            self.price_per_day = 500
            self.who = "owner_share"
        elif type == "baby_seat":
            self.price_per_day = 200
            self.who = "owner_share"
        elif type == "additional_insurance":
            self.price_per_day = 1000
            self.who = "drivy_fee"
        else:
            raise ValueError('type not known')
