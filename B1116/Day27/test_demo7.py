import pytest

@pytest.mark.parametrize('cname',['Ashuthosh','Navyanth','Naresh','Kumar','Punit','Nishchita',True])
def test_create_customer(cname):
    print('create customer',cname)
