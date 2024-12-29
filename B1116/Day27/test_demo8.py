import pytest

@pytest.mark.parametrize(['un','pw'],[('Ashuthosh','A123'),('Nishchitha',123),('Sushma','S123')])
def test_create_customer(un,pw):
    print('create customer',un,pw)
