import pytest

@pytest.fixture(autouse=True)
def login():
    print('\nlogin') #before the test
    yield
    print('\nlogout') #after the test

def test_create_customer():
    print('create customer')

def test_create_product():
    print('create product')

