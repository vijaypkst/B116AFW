fruits=['chiku','apple','banana','apple','orange']
first=fruits.index('apple')
second=fruits.index('apple',first+1)
print(second)


fruits=['chiku','banana','apple','orange','apple']
first=fruits.index('apple')
second=fruits.index('apple',first+1)
print(second)


fruits=['apple','apple','chiku','banana','orange']
first=fruits.index('apple')
second=fruits.index('apple',first+1)
print(second)

fruits=['apple','apple','chiku','banana','orange']
second=fruits.index('apple',fruits.index('apple')+1)
print(second)