"""Module containing tests for the BankAccount class
Author: Taylor Hancock
Date:   03/10/2025
Class:  SE320 - Software Construction
Assignment: Test Driven Development
"""

import os
import pytest
from bank_account import BankAccount

@pytest.fixture
def basic_account(request) -> BankAccount:
    """Creates a default BankAccount with number 1234, owner John Doe, and balance of 500
    Initial balance can be changed via mark.parameterize as shown below"""
    # if not passed in via indirect parameterization, default balance to 500
    # (I'm sure there's a more elegant way to do this within PyTest, but I could not find it)
    if hasattr(request, "param"):
        balance = request.param
    else:
        balance = 500

    account = BankAccount(1234, "John Doe", balance)
    yield account
    account.delete_account()

@pytest.mark.parametrize("basic_account, balance", [(-100,    0),
                                                    (   0,    0),
                                                    ( 500,  500),
                                                    (1000, 1000)], indirect=["basic_account"])
def test_init(basic_account: BankAccount, balance: float) -> None:
    """Tests if the account is created correctly"""

    assert basic_account.balance == balance, \
        "Account created with incorrect balance"
    assert basic_account.balance >= 0, \
        "Account has negative balance"
    assert basic_account.owner == "John Doe", \
        "Account created with incorrect name"
    assert not basic_account.transactions, \
        "New account already has transactions"
    assert basic_account.account_number == 1234, \
        "Account has invalid account number"

def test_to_json(basic_account: BankAccount) -> None:
    """Tests if JSON is correctly parsed and saved by to_json"""
    basic_account.deposit(100)
    basic_account.withdraw(100)

    basic_account.to_json()
    # no error handling needed, if it fails, then something went wrong
    with open(f"{basic_account.account_number}.json", "r") as f:
        json_out = f.readline()

        # check that JSON is correct
        assert json_out == '{"account_number": 1234, "owner": "John Doe", "balance": 500, "transactions": ["Deposit of ¤100", "Withdraw of ¤100"]}', "JSON not correctly saved to file"


def test_from_json(basic_account: BankAccount) -> None:
    """Tests if JSON is correctly loaded and output by from_json"""
    basic_account.deposit(100)
    basic_account.withdraw(100)

    # delete json if it exists
    try:
        os.remove(f"{basic_account.account_number}.json")
    except OSError:
        pass

    # ensure error doesn't occur when from_json is called before to_json
    assert basic_account.from_json() is None

    basic_account.to_json()

    account_dict = basic_account.from_json()

    assert basic_account.balance == account_dict["balance"], \
        "Account balance not copied correctly"
    assert basic_account.owner == account_dict["owner"], \
        "Account owner not copied correctly"
    assert basic_account.transactions == account_dict["transactions"], \
        "Account transactions not copied correctly"
    assert basic_account.account_number == account_dict["account_number"], \
        "Account number broken in copy"


@pytest.mark.parametrize("deposit_amount, is_valid, is_logged, error_response", [
                            ( 100,  True,  True, None),
                            (   0,  True, False, None),
                            (-100, False, False, "Negative deposits are invalid!")
                        ])
def test_deposit(basic_account: BankAccount, deposit_amount: float, is_valid: bool, is_logged: bool,
                 error_response: str | None) -> None:
    """Tests if the deposit function works correctly
    Deposits of zero currency shouldn't affect the balance or be logged as transactions
    Positive deposits should occur and get logged
    Negative deposits should raise a ValueError and not be logged
    """
    initial_balance = basic_account.balance

    # default to no transactions for easier testing
    basic_account.transactions.clear()

    if is_valid: # if valid, run normal test 

        # verify amount is added to total
        basic_account.deposit(deposit_amount)
        assert basic_account.balance == initial_balance + deposit_amount

    else: # if invalid, run error checking test

        # verify correct error is raised
        with pytest.raises(Exception) as e:
            basic_account.deposit(deposit_amount)
        assert e.errisinstance(ValueError), "ValueError not raised on invalid deposit"
        assert str(e.value) == error_response, "Incorrect ValueError raised"

    # check if logged correctly
    # NOTE: There are other ways to handle this, but this way we achieve a more useful error log
    if is_logged:
        assert len(basic_account.transactions) == 1, "Transaction not added to log"
    else:
        assert len(basic_account.transactions) == 0, \
            "Transaction added to log despite no transaction occurring"


@pytest.mark.parametrize("deposit_amount, is_valid, is_logged, error_response", [
                            ( 100,  True,  True, None),
                            (   0,  True, False, None),
                            (-100, False, False, "Negative withdraws are invalid!"),
                            (1000, False, False, "Oversized withdraws (balance < 0) are invalid!")
                        ])
def test_withdraw(basic_account: BankAccount, deposit_amount: float, is_valid: bool, is_logged: bool,
                  error_response: str | None) -> None:
    """Tests if the withdraw function works correctly
    Withdraws of zero currency shouldn't affect the balance or be logged as transactions
    Positive withdraws should occur and get logged if they are less than or equal to the total balance
    Oversized withdraws (greater than the current balance) should raise a ValueError and not be logged
    Negative withdraws should raise a ValueError and not be logged
    """
    initial_balance = basic_account.balance

    # default to no transactions for easier testing
    basic_account.transactions.clear()

    # run normal test if valid, if invalid, run error checking test
    if is_valid:
        # verify amount is added to total
        basic_account.withdraw(deposit_amount)
        assert basic_account.balance == initial_balance - deposit_amount
    else:
        # verify correct error is raised
        with pytest.raises(Exception) as e:
            basic_account.withdraw(deposit_amount)
        assert e.errisinstance(ValueError), "ValueError not raised on invalid deposit"
        assert str(e.value) == error_response, "Incorrect ValueError raised"

    # check if logged correctly
    # NOTE: There are other ways to handle this, but this way we achieve a more useful error log
    if is_logged:
        assert len(basic_account.transactions) == 1, "Transaction not added to log"
    else:
        assert len(basic_account.transactions) == 0, \
            "Transaction added to log despite no transaction occurring"


def test_get_balance(basic_account: BankAccount) -> None:
    """Tests if get_balance returns the correct value"""
    assert basic_account.balance == basic_account.get_balance(), \
        "Output of get_balance is not the actual balance"
