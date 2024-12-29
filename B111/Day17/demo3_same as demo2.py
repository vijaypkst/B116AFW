#write a code to check if given fruit is present in the list or not
#without using in operator
fruit_list=['Apple','Banana','Chiku','Mango']
expected=input('plz enter the fruit name:')
msg = 'Not Found'
for fruit in fruit_list:
    if expected==fruit:
        msg='Found'
        break

print(expected,msg)

