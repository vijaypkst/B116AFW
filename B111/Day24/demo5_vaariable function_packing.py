def f1(a):
    print(type(a),a)

# f1()
f1(10)
# f1(10,20)

def f2(*a):
    print(type(a), a)
    print(len(a))
    for i in a:
        print(i)
f2()
f2(10)
f2(10,20)
f2(10,20,30)