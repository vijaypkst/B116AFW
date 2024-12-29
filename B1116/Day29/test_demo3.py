import pytest

def login():
    print('login')
def logout():
    print('logout')
def test_create_customer():
    login()
    print('create customer')
    logout()


def test_create_product():
    login()
    print('create product')
    logout()


def test_create_user():
    login()
    print('create user')
    logout()
