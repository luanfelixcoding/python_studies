class Bicycle:
    def __init__(self, color, model, year, price):
        self.color = color
        self.model = model
        self.year = year
        self.price = price
        self.gear = 1

    def honk(self):
        print("Honk! Honk!")

    def stop(self):
        print("Stopping...")

    def ride(self):
        print("Riding...")

    def change_gear(self, gear):
        self.gear = gear
        if self.gear > 5:
            self.gear = 5
            print("Gear limit reached")
        else:
            print(f"Changing gear to {self.gear}")
            self.gear += 1

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


bicycle = Bicycle("Red", "Mountain", 2020, 1000)
print(bicycle)
bicycle.change_gear(1)
bicycle.change_gear(2)
bicycle.change_gear(3)
bicycle.change_gear(4)
bicycle.change_gear(5)
bicycle.change_gear(6)
bicycle.honk()
bicycle.ride()
bicycle.stop()
