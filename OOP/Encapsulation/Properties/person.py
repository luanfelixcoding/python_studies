class Person:
    def __init__(self, name: str, brth_year: int) -> None:
        self._name = name
        self._brth_year = brth_year

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        from datetime import datetime
        _current_year: int = datetime.now().year

        return _current_year - self._brth_year


person = Person("Random", 1950)
print(f"Name: {person.name} \tIdade: {person.age}")
