from src import BankAccount
import pytest

@pytest.fixture
def basic_account():
    return BankAccount(1234, "John Doe", 500)

def test_from_json():
    pass

def test_to_json():
    pass

def test_deposit():
    pass

def test_withdraw():
    pass

def test_get_balance():
    pass

def test_show_transactions():
    pass
