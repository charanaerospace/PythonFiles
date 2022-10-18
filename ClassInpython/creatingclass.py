# class name
class Car:
    # attributes
    model = 2020
    mileage = 35
    speed   = 120
    # Methods
    def accelerate(self):
        return Car.speed + 50
    
    def brake(self):
        return Car.speed - 70
car1= Car()
print(car1)
print(car1.accelerate())
print(car1.brake())
print(car1.model)    