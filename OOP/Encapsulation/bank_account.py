class Account:
    def __init__(self, num_agency: str, amount: float = 0) -> None:
        self._amount = amount
        self.num_agency = num_agency

    def deposit(self, value: float) -> None:
        self._amount += value

    def withdraw(self, value: float) -> None:
        if value > self._amount:
            raise ValueError("Impossible to withdraw this value!")
        self._amount -= value

    def show_amount(self) -> float:
        return self._amount


account = Account("0001", 100)
account.deposit(100)
print(account.num_agency)
print(account.show_amount())
