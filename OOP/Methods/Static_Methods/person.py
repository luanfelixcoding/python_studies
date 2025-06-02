from datetime import datetime


class Person:
    def __init__(self, name: str = None, age: int = None) -> None:
        self.name = name
        self.age = age

    @classmethod
    def create_by_birth(cls, year: int, month: int, day: int, name):
        age = datetime.now().year - year
        return cls(name, age)

    @staticmethod
    def is_greater(age: int) -> bool:
        return age >= 18


p = Person.create_by_birth(1994, 3, 21, "John")
print(p.name, p.age)


print(Person.is_greater(18))
print(Person.is_greater(8))
