import pytest
@pytest.fixture(autouse=True,scope="package")
def my_fixture_pkg2():
    print('\nstart pkg2') #before start of pytest session
    yield
    print('\nend pkg2') #after end of pytest session
