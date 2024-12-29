food1=frozenset({'idly','dose','poori'})
food2=frozenset({'idly','dose'})
food3=frozenset({'milk','tea'})
food4=frozenset({'idly','pongal'})
food5=frozenset({'idly','dose','poori','pongal'})
print(food2.issubset(food1)) #all items of food2 is present in  food1
print(food3.issubset(food1))
print(food4.issubset(food1))
print(food5.issubset(food1))
#food1 is subset of food5
#food5 is super set of food1
print(food5.issuperset(food1)) #food5 contains all the elements of food1

