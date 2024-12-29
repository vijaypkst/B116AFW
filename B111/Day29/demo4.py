class Account:
    __balance=1000

    @classmethod
    def set_balance(cls):
        amount=int(input('plz enter the amount'))
        if amount>0:
            Account.__balance=Account.__balance+amount
            print('new balance is',Account.__balance)
        else:
            print('invalid amount')


Account.set_balance()

class Account:
    balance = 1000


Account.balance=5000
print(Account.balance)





