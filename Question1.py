# Base class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def start_engine(self):
        print(f"{self.name}: Starting generic vehicle engine...")

# Subclass Car
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.name}: Vroom! Car engine started.")

# Subclass Bike
class Bike(Vehicle):
    def start_engine(self):
        print(f"{self.name}: Brrrm! Bike engine started.")
