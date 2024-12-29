#write a code to check if given fruit is present in the list or not
#without using in operator
fruit_list=['Apple','Banana','Chiku','Mango']
expected='papaya'
msg=''
for fruit in fruit_list:
    if expected==fruit:
        msg='Found'
        break
    else:
       msg='Not Found'

print(expected,msg)

