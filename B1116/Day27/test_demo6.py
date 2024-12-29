import pytest

@pytest.mark.dependency(name="test_login")
def test_login():
    print('login')


@pytest.mark.dependency(name="test_create_customer")
def test_create_customer():
    print('create customer')


#run delete customer only if both login AND create customer is pass
@pytest.mark.dependency(depends=["test_login","test_create_customer"])
def test_delete_customer():
    print('delete customer')
