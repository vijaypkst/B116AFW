food1=frozenset({'idly','dose','poori'})
food2=frozenset({'idly','dose'})
food3=frozenset({'milk','tea'})

print(food1.isdisjoint(food2)) #False --Not common ? no#Compare two set if common element is found then return false
print(food1.isdisjoint(food3)) #True
