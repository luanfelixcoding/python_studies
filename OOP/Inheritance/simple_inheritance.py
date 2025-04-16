class Vehicle:
    def __init__(self, color: str, plate: str, num_tires: int):
        self.color = color
        self.plate = plate
        self.num_tires = num_tires

    def turn_on(self):
        print(f"Starting engine {self.__class__.__name__}...")

    def turn_off(self):
        print("Stopping engine...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"


class Motorcycle(Vehicle):
    pass


class Car(Vehicle):
    pass


class Truck(Vehicle):
    def __init__(self, color: str, plate: str, num_tires: int, loaded: bool = False):
        # Taking the vehicle __init__ variables
        super().__init__(color, plate, num_tires)

        # Adding specific variable for Truck
        self.loaded = loaded

    # Creating a function specific for truck verifying if truck is loaded
    def is_loaded(self):
        print(
            f"Truck {self.plate} is {f'loaded' if self.loaded else 'not loaded'}")


motorcycle = Motorcycle("Red", "ABC123", 2)
car = Car("Blue", "DEF456", 4)
truck = Truck("Green", "GHI789", 6)


print(motorcycle)
print(car)
print(truck)
