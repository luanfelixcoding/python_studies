class Animal:
    def __init__(self, num_paws: int) -> None:
        self.num_paws = num_paws

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"


class Mammal(Animal):
    def __init__(self, fur_color: str, **kwargs) -> None:
        self.fur_color = fur_color
        super().__init__(**kwargs)

    # def __str__(self) -> str:
    #    return "Mamifero"


class Bird(Animal):
    """ 
    Use '**kwargs' when you wanna take many parameters from father inheritance
    Instead of coding (self, parameter_1, parameter_2, parameter_3, ...)
    Code (self, **kwargs): super().__init__(**kwargs)
    """

    def __init__(self, beak_color: str, **kwargs) -> None:
        self.beak_color = beak_color
        super().__init__(**kwargs)

    # def __str__(self) -> str:
    #    return "Ave"


class Dog(Mammal):
    ...


class Platypus(Mammal, Bird):
    def __init__(self, beak_color: str, fur_color: str, num_paws: int) -> None:
        # print(Platypus.__mro__) # MRO - Method Resolution Order
        # print(Platypus.mro())

        super().__init__(
            fur_color=fur_color, beak_color=beak_color, num_paws=num_paws)

    # def __str__(self) -> str:
    #    return "Ornitorrinco"


dog = Dog(num_paws=4, fur_color="Brown")
print(dog)

platypus = Platypus(num_paws=4, fur_color="Red", beak_color="Orange")
print(platypus)
