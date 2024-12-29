s1=frozenset({10,20,30,40})
s2=frozenset({30,40,50,60})

s3=s1.copy() #create another copy of s1 --> s3

s4=s1.union(s2)
print(s1)#10 20 30 40
print(s2)#30 40 50 60
print(s4)

s5=s1.intersection(s2)
print(s5)


