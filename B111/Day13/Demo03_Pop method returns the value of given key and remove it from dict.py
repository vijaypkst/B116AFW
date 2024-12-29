a={"apple":10,"mango":20,"chiku":30,"apple":15}
print(a)

deleted=a.pop('apple')
print(deleted)

print(a)
a.clear()
print(a)

print(a.pop('aks'))  #when key is mentioned not in the dictionary then there will be key  error