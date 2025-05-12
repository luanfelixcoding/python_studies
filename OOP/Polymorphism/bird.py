"""
Different classes with the same method:
"""


class Bird:
    def fly(self): pass


class Pardal(Bird):
    def fly(self):
        print("Pardal flies")


class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly")


def plan_of_fly(bird):
    bird.fly()


plan_of_fly(Pardal())
plan_of_fly(Ostrich())
