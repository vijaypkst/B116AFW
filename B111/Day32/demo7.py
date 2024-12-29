class BankAccount:
    def __init__(self,acn,name,PAN):
        self.acn=acn
        self.name=name
        self.PAN=PAN
    def __eq__(self, other):
        pan1=self.PAN
        pan2=other.PAN
        return pan1==pan2


a1=BankAccount(1,'Bhanu','A123')
a2=BankAccount(2,'Bhanu','B456')
a3=BankAccount(3,'Bhanu P','A123')

print(a1==a2) #false
print(a1==a3) #true