## Overview

In this assignment, you’ll test a Python class that represents a **Bank Account**. You will use **pytest fixtures** to set up and tear down test resources. The goal is to ensure the class behaves correctly for common banking operations like deposits, withdrawals, and balance inquiries, while also handling edge cases gracefully.

This assignment not only reinforces the basics of testing with pytest and encourages to think critically about class behavior and edge cases.

## Learning Objectives

By completing this assignment, you will:
1. Learn to write unit tests for Python classes.
2. Use pytest fixtures to manage setup and teardown of test objects.
3. Practice testing edge cases and error handling.

## The BankAccount Class

Here is the class you will be testing. The BankAccount class should have the following member-variables: account_number, owner, balance, and transactions.

"""
This module contains a class that represents a bank account.
The account supports deposit, withdraw, and get_balance operations.
Serialization and deserialization of the account is implemented using json.
"""
class BankAccount:
    """A simple BankAccount class with methods to deposit, withdraw, and get_balance."""
    
    def __init__(self, account_number, owner=""):
       """Initialize a BankAccount with an owner and an optional starting balance."""
        ...

    def from_json(self) -> dict | None:
        """Deserialize a BankAccount object from a json file."""
        ...

    def to_json(self):
       """Serialize a BankAccount object to a json file."""
       ...

    def deposit(self, amount):
       """Deposit a positive amount to the account."""
        ...

    def withdraw(self, amount):
       """Withdraw a positive amount if sufficient balance exists."""
        ...

    def get_balance(self):
       """Return the current balance."""
        ...
        
     def show_transactions(self):
         """Prints all account transactions."""

## Assignment Requirements

    Write Test Cases
        Create a test_bank_account.py file.
        Write unit tests for the BankAccount class using pytest fixtures for setup and teardown.

    Use Fixtures
        Create a pytest fixture to initialize a BankAccount instance before each test.
        Add parameters to the fixture for different starting balances if needed.

    Test Scenarios
    Write tests to cover the following scenarios:
        Deposit Method:
            Depositing a valid amount increases the balance.
            Depositing a non-positive amount raises a ValueError.
        Withdraw Method:
            Withdrawing a valid amount decreases the balance.
            Withdrawing more than the current balance raises a ValueError.
            Withdrawing a non-positive amount raises a ValueError.
        Get Balance Method:
            Returns the correct current balance.

    Edge Cases
        Test edge cases, such as depositing or withdrawing a zero amount, or initializing the account with a negative balance.

Deliverables

    A tdd.zip file containing bank_account.py and test_bank_account.py file.
    Output: Provide a text or Markdown file with the output of running pytest on your test file (e.g., pytest --tb=short).

## Evaluation Criteria
| Criteria                                   | Points |
|--------------------------------------------|--------|
| Correct BankAccount class implementation   | 1      |
| Correct implementation of pytest fixture 	 | 1      |
| Tests for deposit functionality            | 1      |
| Tests for withdraw functionality           | 1      |
| Tests for get_balance functionality        | 1      |
| Tests for (de-)serialization functionality | 2      |
| Handling of edge cases                     | 1      |
| Clean code and meaningful assertions       | 1      |
| All methods have correct type hints        | 1      |