from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum


class TransactionType(Enum):
    DEPOSIT = "Deposit"
    WITHDRAWAL = "Withdrawal"


class Client:
    """Represents a bank client."""

    def __init__(self, address: str) -> None:
        self.address = address
        # Using 'Account' for forward reference
        self.accounts: list['Account'] = []

    def perform_transaction(self, account: 'Account', transaction: 'Transaction') -> None:
        """Performs a transaction on an account."""
        transaction.register(account)

    def add_account(self, account: 'Account') -> None:
        """Adds a new account to the client."""
        self.accounts.append(account)


class Individual(Client):
    """Represents an individual person, a specific type of client."""

    def __init__(self, name: str, date_of_birth: str, cpf: str, address: str) -> None:
        super().__init__(address)
        self.name = name
        self.date_of_birth = date_of_birth
        self.cpf = cpf


class Account:
    """Represents a bank account."""

    def __init__(self, number: int, client: Client) -> None:
        self._balance = 0.0
        self._number = number
        self._agency = "0001"
        self._client = client
        self._history = History()

    @classmethod
    def new_account(cls, client: Client, number: int) -> 'Account':
        """Creates a new account instance."""
        return cls(number, client)

    @property
    def balance(self) -> float:
        """Returns the account balance."""
        return self._balance

    @property
    def number(self) -> int:
        """Returns the account number."""
        return self._number

    @property
    def agency(self) -> str:
        """Returns the account agency."""
        return self._agency

    @property
    def client(self) -> Client:
        """Returns the client associated with the account."""
        return self._client

    @property
    def history(self) -> 'History':
        """Returns the account transaction history."""
        return self._history

    def withdraw(self, value: float) -> bool:
        """Performs a withdrawal from the account."""
        balance = self.balance
        exceeded_balance = value > balance

        if exceeded_balance:
            print("\n@@@ Operation failed! You don't have sufficient balance. @@@")
            return False
        elif value <= 0:
            print("\n@@@ Operation failed! The informed value is invalid. @@@")
            return False
        else:
            self._balance -= value
            print("\n=== Withdrawal performed successfully! ===")
            return True

    def deposit(self, value: float) -> bool:
        """Performs a deposit into the account."""
        if value > 0:
            self._balance += value
            print("\n=== Deposit performed successfully! ===")
            return True
        else:
            print("\n@@@ Operation failed! The informed value is invalid. @@@")
            return False


class CheckingAccount(Account):
    """Represents a checking account, with a limit and withdrawal limit."""

    def __init__(self, number: int, client: Client, limit: float = 500.0, withdrawal_limit: int = 3) -> None:
        super().__init__(number, client)
        self.limit = limit
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, value: float) -> bool:
        """Performs a withdrawal from the checking account, considering limits."""
        number_of_withdrawals = len(
            [transaction for transaction in self.history.transactions if transaction["type"]
                == TransactionType.WITHDRAWAL.value]
        )

        exceeded_limit = value > self.limit
        exceeded_withdrawals = number_of_withdrawals >= self.withdrawal_limit

        if exceeded_limit:
            print("\n@@@ Operation failed! The withdrawal value exceeds the limit. @@@")
            return False
        elif exceeded_withdrawals:
            print("\n@@@ Operation failed! Maximum number of withdrawals exceeded. @@@")
            return False
        else:
            return super().withdraw(value)

    def __str__(self) -> str:
        """Returns a string representation of the checking account."""
        return f"""\
            Agency:\t\t{self.agency}
            Account No.:\t{self.number}
            Holder:\t\t{self.client.name}
        """


class History:
    """Records the transaction history of an account."""

    def __init__(self) -> None:
        self._transactions: list[dict] = []

    @property
    def transactions(self) -> list[dict]:
        """Returns the list of transactions."""
        return self._transactions

    def add_transaction(self, transaction: 'Transaction') -> None:
        """Adds a transaction to the history."""
        self._transactions.append(
            {
                "type": transaction.type.value,  # Using the Enum value
                "value": transaction.value,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transaction(ABC):
    """Abstract base class for all transactions."""

    @property
    @abstractmethod
    def value(self) -> float:
        """Returns the transaction value."""
        pass

    @property
    @abstractmethod
    def type(self) -> TransactionType:
        """Returns the transaction type."""
        pass

    @abstractmethod
    def register(self, account: Account) -> None:
        """Registers the transaction in an account."""
        pass


class Withdrawal(Transaction):
    """Represents a withdrawal transaction."""

    def __init__(self, value: float) -> None:
        self._value = value

    @property
    def value(self) -> float:
        """Returns the withdrawal value."""
        return self._value

    @property
    def type(self) -> TransactionType:
        """Returns the transaction type as Withdrawal."""
        return TransactionType.WITHDRAWAL

    def register(self, account: Account) -> None:
        """Registers the withdrawal in the account."""
        transaction_success = account.withdraw(self.value)

        if transaction_success:
            account.history.add_transaction(self)


class Deposit(Transaction):
    """Represents a deposit transaction."""

    def __init__(self, value: float) -> None:
        self._value = value

    @property
    def value(self) -> float:
        """Returns the deposit value."""
        return self._value

    @property
    def type(self) -> TransactionType:
        """Returns the transaction type as Deposit."""
        return TransactionType.DEPOSIT

    def register(self, account: Account) -> None:
        """Registers the deposit in the account."""
        transaction_success = account.deposit(self.value)

        if transaction_success:
            account.history.add_transaction(self)


def display_menu() -> str:
    """Displays the main menu options and returns the user's choice."""
    menu = """\n
    =============== BANK MENU ===============
    [d]\t\tDeposit
    [w]\t\tWithdraw
    [s]\t\tStatement
    [na]\tNew Account
    [lc]\tList Clients
    [la]\tList Accounts
    [nc]\tNew Client
    [q]\t\tQuit
    =========================================
    => """
    return input(menu)


def filter_client(cpf: str, clients: list[Client]) -> Client | None:
    """Filters clients by CPF and returns the matching client or None."""
    for client in clients:
        if isinstance(client, Individual) and client.cpf == cpf:
            return client
    return None


def filter_account(client: Client, number: int) -> Account | None:
    """Filters client's accounts by number and returns the matching account or None."""
    for account in client.accounts:
        if account.number == number:
            return account
    return None


def create_client(clients: list[Client]) -> None:
    """Creates a new individual client."""
    cpf = input("Enter CPF (numbers only): ")
    client = filter_client(cpf, clients)

    if client:
        print("\n@@@ Error: There is already a client with this CPF! @@@")
        return

    name = input("Enter full name: ")
    date_of_birth = input("Enter date of birth (dd-mm-yyyy): ")
    address = input(
        "Enter address (street, number - neighborhood - city/state): ")

    new_client = Individual(
        name=name, date_of_birth=date_of_birth, cpf=cpf, address=address)
    clients.append(new_client)
    print("\n=== Client created successfully! ===")


def create_account(account_number: int, clients: list[Client], accounts: list[Account]) -> None:
    """Creates a new checking account for an existing client."""
    cpf = input("Enter client's CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n@@@ Error: Client not found! @@@")
        return

    new_account = CheckingAccount.new_account(
        client=client, number=account_number)
    client.add_account(new_account)
    accounts.append(new_account)
    print("\n=== Account created successfully! ===")


def perform_deposit(clients: list[Client]) -> None:
    """Handles the deposit operation."""
    cpf = input("Enter client's CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n@@@ Error: Client not found! @@@")
        return

    account_number = int(input("Enter account number: "))
    account = filter_account(client, account_number)

    if not account:
        print("\n@@@ Error: Account not found for this client! @@@")
        return

    value = float(input("Enter the deposit amount: "))
    transaction = Deposit(value)
    client.perform_transaction(account, transaction)


def perform_withdrawal(clients: list[Client]) -> None:
    """Handles the withdrawal operation."""
    cpf = input("Enter client's CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n@@@ Error: Client not found! @@@")
        return

    account_number = int(input("Enter account number: "))
    account = filter_account(client, account_number)

    if not account:
        print("\n@@@ Error: Account not found for this client! @@@")
        return

    value = float(input("Enter the withdrawal amount: "))
    transaction = Withdrawal(value)
    client.perform_transaction(account, transaction)


def display_statement(clients: list[Client]) -> None:
    """Displays the statement (transaction history) for an account."""
    cpf = input("Enter client's CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n@@@ Error: Client not found! @@@")
        return

    account_number = int(input("Enter account number: "))
    account = filter_account(client, account_number)

    if not account:
        print("\n@@@ Error: Account not found for this client! @@@")
        return

    print("\n============== STATEMENT ==============")
    transactions = account.history.transactions

    if not transactions:
        print("No transactions were made for this account.")
    else:
        for transaction in transactions:
            print(
                f"{transaction['type']}:\t\tR$ {transaction['value']:.2f} ({transaction['date']})")

    print(f"\nBalance:\t\tR$ {account.balance:.2f}")
    print("========================================")


def list_accounts(accounts: list[Account]) -> None:
    """Lists all registered accounts."""
    if not accounts:
        print("\n@@@ No accounts registered yet! @@@")
        return

    for account in accounts:
        print("=" * 100)
        print(str(account))
    print("=" * 100)


def list_clients(clients: list[Client]) -> None:
    """Lists all registered clients."""
    if not clients:
        print("\n@@@ No clients registered yet! @@@")
        return

    for client in clients:
        print("=" * 100)
        print(f"Name:\t\t{client.name}")
        print(f"CPF:\t\t{client.cpf}")
        print(f"Address:\t{client.address}")
        print(f"Date of Birth:\t{client.date_of_birth}")
    print("=" * 100)


def main():
    """Main function to run the banking system."""
    clients: list[Client] = []
    accounts: list[Account] = []
    account_counter = 1

    while True:
        option = display_menu()

        if option == "d":
            perform_deposit(clients)
        elif option == "w":
            perform_withdrawal(clients)
        elif option == "s":
            display_statement(clients)
        elif option == "nc":
            create_client(clients)
        elif option == "na":
            create_account(account_counter, clients, accounts)
            account_counter += 1
        elif option == "lc":
            list_clients(clients)
        elif option == "la":
            list_accounts(accounts)
        elif option == "q":
            print("\nExiting the system. Thank you!")
            break
        else:
            print("\n@@@ Invalid option, please try again! @@@")


if __name__ == "__main__":
    main()
