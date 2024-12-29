import pytest

@pytest.fixture(autouse=True)
def login():
    print('\nlogin')

def test_create_customer():
    print('create customer')

def test_create_product():
    print('create product')

def test_create_user():
    print('create user')
