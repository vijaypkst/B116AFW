#print small names (size <=4)
students=['Vani','Prakash','CHANDRA','Ravi','Vijay']
for name in students:
    if len(name)>4:
        continue
    print(name)