class Vehicle:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def move(self) -> None:
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self) -> None:
        print("Sail!")


class Plane(Vehicle):
    def move(self) -> None:
        print("Take Off!")


car = Car("Ford", "F-150")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "747")

for object in (car, boat, plane):
    print(f"Brand: {object.brand}\tModel: {object.model}", end="\t")
    object.move()
