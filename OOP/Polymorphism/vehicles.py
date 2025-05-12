"""
Different classes with the same method:
"""


class Car:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def move(self) -> None:
        print("Drive!")


class Boat:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def move(self) -> None:
        print("Sail!")


class Plane:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def move(self) -> None:
        print("Fly!")


car = Car("Ford", "Mustang")  # Create a Car object
boat = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane = Plane("Boeing", "747")  # Create a Plane object

for object in (car, boat, plane):
    object.move()
