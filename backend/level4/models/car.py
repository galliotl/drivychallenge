class Car:
    def __init__(self, id, price_per_km, price_per_day):
        assert price_per_day >= 0 and price_per_km >= 0
        self.id = id
        self.price_per_km = price_per_km
        self.price_per_day = price_per_day
