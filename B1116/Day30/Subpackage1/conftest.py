import pytest
@pytest.fixture(autouse=True,scope="package")
def my_fixture_pkg1():
    print('\nstart pkg1') #before start of pytest session
    yield
    print('\nend pkg1') #after end of pytest session
