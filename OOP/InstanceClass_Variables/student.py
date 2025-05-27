class Student:
    university: str = "Harvard" # Variable of class

    def __init__(self, name: str, num_regis: int) -> None:
        self.name = name
        self.num_regis = num_regis

    def __str__(self) -> str:
        return f"{self.name} ({self.university}) - {self.num_regis}"


def show_values(*objects: object) -> None:
    for obj in objects:
        print(obj)
    print()


std_1 = Student("John", 32325)
std_2 = Student("Anna", 55231)
show_values(std_1, std_2)

Student.name = "Stanford" # Here it shows that we cannot modify the parameter in init(), only outside of it
Student.university = "Stanford" # Modifying the variable 'university' of the class
std_3 = Student("Chappie", 90909)
show_values(std_1, std_2, std_3)