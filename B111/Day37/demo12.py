list1=['IBM','Infosys','TCS','Wipro','ABB']
list2=[name for name in list1 if name.isupper()]
print(list2)


def is_upper(name):
    return name.isupper()

list2=list(filter(is_upper,list1))
print(list2)