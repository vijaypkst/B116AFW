a=[10,20,30,40]
print(a)
a.pop(0)
print(a)

a.pop(-1)
print(a)

a.pop(3) #IndexError: pop index out of range
print(a)
