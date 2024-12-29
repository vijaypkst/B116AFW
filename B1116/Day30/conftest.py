import pytest
@pytest.fixture(autouse=True,scope="package")
def my_fixture():
    print('\nprecondition') #before every test
    yield
    print('\npostcondition') #after every test
