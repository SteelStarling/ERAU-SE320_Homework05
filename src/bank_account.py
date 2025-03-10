"""
This module contains a class that represents a bank account.
The account supports deposit, withdraw, and get_balance operations.
Serialization and deserialization of the account is implemented using json.
"""
class BankAccount:
    """A simple BankAccount class with methods to deposit, withdraw, and get_balance."""
    
    def __init__(self, account_number: int, owner: str = "", balance: float = 0.0):
        """Initialize a BankAccount with an owner and an optional starting balance."""
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def delete_account(self):
        """Remove all items in account"""
        self.account_number = 0
        self.owner = ""
        self.balance = 0
        self.transactions.clear()

    def from_json(self) -> dict | None:
        """Deserialize a BankAccount object from a json file."""
        pass

    def to_json(self) -> str:
        """Serialize a BankAccount object to a json file."""
        pass

    def deposit(self, amount: float):
        """Deposit a positive amount to the account."""
        pass

    def withdraw(self, amount: float):
        """Withdraw a positive amount if sufficient balance exists."""
        pass

    def get_balance(self) -> float:
        """Return the current balance."""
        return self.balance
        
    def show_transactions(self):
        """Prints all account transactions."""
        print(self.transactions)
