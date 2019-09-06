import datetime

class Rental:
    def __init__(self, id, start_date, end_date, distance, car_id):
        self.id = id
        assert distance >= 0
        self.distance = distance
        self.car_id = car_id
        
        # we add 1 because the first day is also billed
        try:
            self.duration = datetime.datetime.strptime(end_date, '%Y-%m-%d') - datetime.datetime.strptime(start_date, '%Y-%m-%d')
        except:
            raise ValueError("Rental duration can't be computed with the given values")
        else:
            assert self.duration.days >= 0
            self.duration = 1 + self.duration.days
