import pytest

#to send data while yielding
@pytest.fixture()
def f1():
   print('Start Fixture')
   i=10
   yield i
   print('End Fixture')


def test1(f1):
    i=f1
    print('this is test1:',i)