import pytest


@pytest.mark.dependency(name="test_create_customer")
def test_create_customer():
    print('create customer')
    assert False


@pytest.mark.dependency(depends=["test_create_customer"])
def test_delete_customer():
    print('delete customer')
