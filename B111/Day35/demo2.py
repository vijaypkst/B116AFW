print('Start')
a=input('Please enter a number')
try:
    b=int(a) #risky code
    c=b+b
    print(c)
except:
    print('I got error') #recovery code

print('End')