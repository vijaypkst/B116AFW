def f1(*a):
    print(len(a),a)
   # for i in a:
   #     print(i)


list1=[10,20,30]
list2=[40,50,60]

f1(*list1,*list2)


f1(list1,list2)


