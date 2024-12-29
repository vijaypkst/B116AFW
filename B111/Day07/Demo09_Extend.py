a=[10,20]
b=[30,40]
a.append(b)  # will insert entire list in a list
print(a)

a=[10,20]
b=[30,40]
a.extend(b)  # to insert the list /merge the list
print(a)