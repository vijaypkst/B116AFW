#diff ways of creating tuple
a=() #empty tuple
print(type(a),a,len(a))

a=(10,20,4)
print(type(a),a,len(a))

a=tuple()
print(type(a),a,len(a))

a=tuple(range(4))
print(type(a),a,len(a))

a=tuple(range(1,10,2))
print(type(a),a,len(a))

a=(10,20,30)*3
print(type(a),a,len(a))

p=[10,20,30]
a=tuple(p) #convert list to tuple
print(type(a),a,len(a))

