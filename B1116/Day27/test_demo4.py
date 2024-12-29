import pytest

@pytest.mark.run(order=1)
def test_create_customer():
    print('create customer')
@pytest.mark.run(order=3)
def test_edit_customer():
    print('edit customer')

@pytest.mark.run(order=2)
def test_copy_customer():
    print('copy customer')

@pytest.mark.run(order=4)
def test_delete_customer():
    print('delete customer')
