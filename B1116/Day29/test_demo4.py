import pytest

@pytest.fixture()
def login():
    print('\nlogin')


def test_create_customer(login):
    print('create customer')

def test_create_product(login):
    print('create product')

def test_create_user(login):
    print('create user')
