import pytest
@pytest.mark.smoke
@pytest.mark.customer
def test_create_customer():
    print('create customer/n')
@pytest.mark.customer
def test_edit_customer():
    print('edit customer')
@pytest.mark.customer
def test_delete_customer():
    print('delete customer')
@pytest.mark.smoke
@pytest.mark.product
def test_create_product():
    print('create product')
@pytest.mark.product
def test_edit_product():
    print('edit product')
@pytest.mark.product
def test_delete_product():
    print('delete product')
@pytest.mark.smoke
@pytest.mark.user
def test_create_user():
    print('create user')
@pytest.mark.user
def test_edit_user():
    print('edit user')
@pytest.mark.user
def test_delete_user():
    print('delete user')
