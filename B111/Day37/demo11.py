list1=['Akash','Akshara','Rashmi','Bhumi','Ashwin']
list2=[name for name in list1  if name.startswith('B') ]
print(list2)

def is_starts_with_a(name):
    return name.startswith('A')

list2=list(filter(is_starts_with_a,list1))
print(list2)