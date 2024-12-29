food1=frozenset({'idly','dose','poori'})
food2=frozenset({'idly','dose'})
food3=frozenset({'idly','dose','pongal'})

print(food2.issubset(food1)) #all items of food2 is present in food1? yes
print(food2.isdisjoint(food1)) #food2 and food1 are completly diff?--No

print(food3.issubset(food1)) #false
print(food3.isdisjoint(food1))#false

