#membership operator
family=['Mom','Papa',"Bro",'Sister']
print('Mom' in family)
print('Uncle' in family)
print('Sis' in family)
print('bro' in family)

family=('Mom','Papa',"Bro",'Sister')
print('Mom' in family)

family= {'Mom','Papa',"Bro",'Sister'}
print('Mom' in family)

#frozent set
family= frozenset({'Mom','Papa',"Bro",'Sister'})
print('Mom' in family)
#dictionary
family= {'Mom':1,'Papa':2}

print('Mom' in family) #key
print(1 in family) #value