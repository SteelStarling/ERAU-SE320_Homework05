from src import BankAccount
import pytest

@pytest.fixture
def basic_account(request = None):
    """Creates a default BankAccount with number 1234, owner John Doe, and balance of 500
    Initial balance can be changed via mark.parameterize as shown below"""
    # if not passed in mark, default balance to 500
    # (I'm sure there's a more elegant way to do this within PyTest, but I could not find it)
    if request.param is None:
        balance = 500
    else:
        balance = request.param
    
    account = BankAccount(1234, "John Doe", balance)
    yield account
    account.delete_account()

@pytest.mark.parametrize("basic_account", [-500, 0, 500], indirect=True)
def test_init(basic_account):
    """Tests if the account is created correctly"""
    pass

def test_from_json():
    pass

def test_to_json():
    pass

@pytest.mark.parametrize("basic_account", [500], indirect=True)
def test_deposit(basic_account):
    """Tests if the deposit function works correctly
    Deposits of zero currency shouldn't affect the balance or be logged as transactions
    Positive deposits should occur and get logged
    Negative deposits should raise a ValueError and not be logged
    """
    initial_balance = basic_account.balance

    positive_deposit =  100
    negative_deposit = -100
    
    # zero amounts should do nothing
    basic_account.deposit(0)
    assert basic_account.balance == initial_balance, "Zero deposits should do nothing"

    # zero amount transactions should not be logged...as they really don't happen
    assert len(basic_account.transactions) == 0, "Transaction added to log despite no transaction occurring"
               
    # valid amounts should increase the balance
    basic_account.deposit(positive_deposit)
    assert basic_account.balance == initial_balance + positive_deposit, "Positive deposits should increase balance"
    assert len(basic_account.transactions) == 1, "Incorrect number of transactions recorded"

    # non-positive amounts raise ValueError
    with pytest.raises(Exception) as e:
        basic_account.deposit(negative_deposit)
    assert e.errisinstance(ValueError), "ValueError not raised on negative deposits"
    assert str(e.value) == "Negative deposits are invalid!", "Incorrect ValueError raised"

    # invalid deposits will not add an item to the transaction list
    assert len(basic_account.transactions) == 1, "Invalid transaction recorded in transaction log"

@pytest.mark.parametrize("basic_account", [500], indirect=True)
def test_withdraw(basic_account):
    """Tests if the withdraw function works correctly
    Withdraws of zero currency shouldn't affect the balance or be logged as transactions
    Positive withdraws should occur and get logged if they are less than or equal to the total balance
    Oversized withdraws (greater than the current balance) should raise a ValueError and not be logged
    Negative withdraws should raise a ValueError and not be logged
    """
    initial_balance = basic_account.balance

    positive_withdraw =   initial_balance  # ensure balance can be set to zero
    negative_withdraw =  -100
    oversized_withdraw =  1000

    # zero amounts should do nothing
    basic_account.withdraw(0)
    assert basic_account.balance == initial_balance, "Zero withdraws should do nothing"

    # zero amount transactions should not be logged...as they really don't happen
    assert len(basic_account.transactions) == 0, "Transaction added to log despite no transaction occurring"

    # valid amounts should decrease the balance (down to a max of zero)
    basic_account.withdraw(positive_withdraw)
    assert basic_account.balance == initial_balance - positive_withdraw, "Positive withdraws should decrease balance"

    # valid withdraw should add an item to the transaction list
    assert len(basic_account.transactions) == 1, "Incorrect number of transactions recorded"

    # withdrawing more than the current balance raises a value error
    with pytest.raises(Exception) as e:
        basic_account.withdraw(oversized_withdraw)
    assert e.errisinstance(ValueError), "ValueError not raised on oversized withdraws"
    assert str(e.value) == "Oversized withdraws (balance < 0) are invalid!", "Incorrect ValueError raised"

    # non-positive amounts raise ValueError
    with pytest.raises(Exception) as e:
        basic_account.withdraw(negative_withdraw)
    assert e.errisinstance(ValueError), "ValueError not raised on negative withdraws"
    assert str(e.value) == "Negative withdraws are invalid!", "Incorrect ValueError raised"

    # invalid withdraws will not add a items to the transaction list
    assert len(basic_account.transactions) == 1, "Invalid transaction recorded in transaction log"

@pytest.mark.parametrize("basic_account", [500], indirect=True)
def test_get_balance(basic_account):
    """Tests if get_balance returns the correct value"""

    # returns correct value
    assert basic_account.balance == basic_account.get_balance(), "Output of get_balance is not the actual balance"
