"""
In Encapsulation subject when you want to protect 
the variable by convention you use only one underscore "_".
When you want to turn the variable PRIVATE you use two underscore "__".
"""


class Base:
    def __init__(self) -> None:
        self._protected = "I am protected"
        self.__private = "I am private"


class Derived(Base):
    def print_vars(self):
        print(self._protected)        # Works
        # print(self.__private)       # AttributeError
        print(self._Base__private)    # Works via name mangling


obj = Derived()
obj.print_vars()
