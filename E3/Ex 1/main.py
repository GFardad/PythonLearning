class vehicle:

    def __init__(self, max_speed, milage, prod_year, brand):
        self.max_speed = 120
        self.milage = 0
        self.prod_year = 2000
        self.brand = "benz"

    def age_calc(self, prod_year=self.prod_year):
        return (2025) - (prod_year)


class bus(vehicle):
    def set_capacity(self, capacity):
        self.seatting_capacity = 100


bus1 = bus(max_speed=100, milage=250, prod_year=2010, brand="Kos")
print(bus1.age_calc())
