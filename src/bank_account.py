"""
This module contains a class that represents a bank account.
The account supports deposit, withdraw, and get_balance operations.
Serialization and deserialization of the account is implemented using json.
"""

import json

class BankAccount:
    """A simple BankAccount class with methods to deposit, withdraw, and get_balance."""

    def __init__(self, account_number: int, owner: str = "", balance: float = 0.0):
        """Initialize a BankAccount with an owner and an optional starting balance."""
        self.account_number = account_number
        self.owner = owner
        self.balance = max(balance, 0) # ensure balance is greater than 0
        self.transactions = []

    def delete_account(self):
        """Remove all items in account"""
        self.account_number = 0
        self.owner = ""
        self.balance = 0
        self.transactions.clear()

    def from_json(self) -> dict | None:
        """Deserialize a BankAccount object from a json file."""
        try:
            with open(f"{self.account_number}.json", "r") as f:
                return json.loads(f.readline())
        except FileNotFoundError:
            return None
    

    def to_json(self):
        """Serialize a BankAccount object to a json file."""
        with open(f"{self.account_number}.json", "w") as f:
            f.write(f'{{"account_number": {self.account_number}, "owner": "{self.owner}", "balance": {self.balance}, "transactions": [')

            # ensure strings wrapped in double quotes (JSON requirement)
            fixed_transactions = [f'"{transaction}"' for transaction in self.transactions]

            # add comma separated transactions to string and close parens
            f.write(", ".join(fixed_transactions) + ']}')


    def deposit(self, amount: float) -> None:
        """Deposit a positive amount to the account."""

        # prevent negative deposits
        if amount < 0:
            raise ValueError("Negative deposits are invalid!")

        # deposit value
        self.balance += amount

        # only add to transactions if not zero
        if amount != 0:
            self.transactions.append(f'Deposit of ¤{amount}')


    def withdraw(self, amount: float) -> None:
        """Withdraw a positive amount if sufficient balance exists."""

        # prevent negative withdraws
        if amount < 0:
            raise ValueError("Negative withdraws are invalid!")

        # prevent withdrawing more than total money (entering debt)
        if amount > self.balance:
            raise ValueError("Oversized withdraws (balance < 0) are invalid!")

        # withdraw value
        self.balance -= amount

        # only add to transactions if not zero
        if amount != 0:
            self.transactions.append(f'Withdraw of ¤{amount}')


    def get_balance(self) -> float:
        """Return the current balance."""
        return self.balance
        
    def show_transactions(self) -> None:
        """Prints all account transactions."""
        for transaction in self.transactions:
            print(transaction)
