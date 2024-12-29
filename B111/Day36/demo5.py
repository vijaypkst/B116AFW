#print 1 2 3 using for loop
class CardIsBlocked(Exception):
    def __init__(self):
        super().__init__("Your CARD is blocked!!")

def login_to_ATM():
    for i in range(1,4):
       pin=int(input('Plz enter ur ATM PIN'))
       if pin==123:
           print('Welcome')
           break
       else:
           if i==3:
              raise CardIsBlocked()
           else:
               print('invalid pin , plz try again')


try:
    login_to_ATM()
except Exception as e:
    print(e)
    print('call customer support')