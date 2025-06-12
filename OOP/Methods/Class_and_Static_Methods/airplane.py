from datetime import datetime


class Airplane:
    # Class variables(attributes)
    _total_airplanes = 0
    _flee_status = {}

    def __init__(self, model: str, capactiy: int, tail_number: str) -> None:
        if not isinstance(model, str) or not model:
            raise ValueError("The airplane model must be a non-empty string.")
        if not isinstance(capactiy, int) or capactiy <= 0:
            raise ValueError(
                "The capacity of the airplane must be a positive integer.")
        if not isinstance(tail_number, str) or not tail_number:
            raise ValueError("The tail number must be a non-empty string.")

        self.model = model
        self.capacity = capactiy
        self.tail_number = tail_number
        self.status = "available"  # Initial status of the airplane

        # Update the class attributes when creating a new instance
        Airplane._total_airplanes += 1
        Airplane._fleet_status[self.tail_number] = self.status
        print(
            f"Avião {self.tail_number} ({self.model}) criado e adicionado à frota.")

    @classmethod
    def get_total_airplanes(cls) -> int:
        return cls._total_airplanes

    @classmethod
    def get_fleet_status(cls) -> dict:
        return cls._flee_status

    @classmethod
    def update_airplane_status(cls, tail_number: str, new_status: str) -> bool:
        if tail_number in cls._flee_status:
            cls._flee_status[tail_number] = new_status
            print(
                f"Airplane tail number {tail_number} status updated for '{new_status}'.")
            return True
        print(
            f"Tail number {tail_number} was not found!.")
        return False

    def fly(self) -> None:
        if self.status == "available":
            self.status = "in flight"
            Airplane.update_airplane_status(self.tail_number, "in flight")
            print(f"Airplane tail number {self.tail_number} is 'in flight'.")
        else:
            print(
                f"Airplane tail number {self.tail_number} cannot fly, current status: {self.status}.")

    def land(self) -> None:
        if self.status == "in flight":
            self.status = "available"
            Airplane.update_airplane_status(self.tail_number, "available")
            print(
                f"Airplane tail number {self.tail_number} landed and it is 'avaiable'.")
        else:
            print(
                f"Airplane tail number {self.tail_number} could not land, current status: {self.status}.")

    def __str__(self) -> str:
        return f"Airplane: {self.model} | Tail: {self.tail_number} | Capacity: {self.capacity} | Status: {self.status}"


boeing = Airplane("boeing 766", 300, "90")

boeing.get_fleet_status()
boeing.get_total_airplanes()

boeing.fly()
boeing.land()
