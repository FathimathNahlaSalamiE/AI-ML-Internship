class Vehicle:
    def start(self):
        print("vehicle starting")
class Car(Vehicle):
    def start(self):
        print("Car starting")

obj = Car()
obj.start()