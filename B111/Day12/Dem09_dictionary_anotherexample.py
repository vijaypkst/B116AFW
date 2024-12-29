#stocks --> items purchased--class room
#board-1 desk-1 duster-2 marker-12 chair-20
#to store this info we cant use
#tuple--> we cant change it
#set--> duplicate not allowed
#frozenset-->no dup no chage..

a=[20,30,10]
print(a)#10 20 30
print(a[0]) #20

b={'desk':20,'marker':30,'board':20,'board':10}
print(type(b),b)
print(b['board'])#10

#----------------------------
a={}
print(type(a))
a={10,20}
print(type(a))

a={10:10,20:20}
print(type(a))
