"""
This module contains a class that represents a bank account.
The account supports deposit, withdraw, and get_balance operations.
Serialization and deserialization of the account is implemented using json.
"""
class BankAccount:
    """A simple BankAccount class with methods to deposit, withdraw, and get_balance."""
    
    def __init__(self, account_number, owner="", balance=0):
        """Initialize a BankAccount with an owner and an optional starting balance."""
        pass

    def from_json(self) -> dict | None:
        """Deserialize a BankAccount object from a json file."""
        pass

    def to_json(self):
        """Serialize a BankAccount object to a json file."""
        pass

    def deposit(self, amount):
        """Deposit a positive amount to the account."""
        pass

    def withdraw(self, amount):
        """Withdraw a positive amount if sufficient balance exists."""
        pass

    def get_balance(self):
        """Return the current balance."""
        pass
        
    def show_transactions(self):
        """Prints all account transactions."""
        pass
