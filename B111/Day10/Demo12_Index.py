msg='rain  rain go away '
first=msg.index('rain')
print(first)
second=msg.index('rain',first+1)
print(second)

print(msg.index('come')) #ValueError: substring not found