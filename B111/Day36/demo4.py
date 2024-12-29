
class MyException(Exception):
   def __init__(self):
       super().__init__('Hi Bhanu this is my own exception')

try:
    raise MyException()
except Exception as e:
    print(e)


class MyException2(Exception):
    def __init__(self,msg):
        super().__init__(msg)


try:
    raise MyException2('This is diff msg')
except Exception as e:
    print(e)
