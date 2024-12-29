import pytest


@pytest.fixture(params=['Apple','Mango','Grapes'])
def precodition(request):
    data=request.param
    print('pre condition',data)


def test_m1(precodition):
    print('Test m1')