import pytest

@pytest.mark.skip
def test_create_customer():
    print('create customer')

a=9
@pytest.mark.skipif(a>=10,reason="because a is ten")
def test_edit_customer():
    print('edit customer')

def test_copy_customer():
    print('copy customer')

def test_delete_customer():
    print('delete customer')

