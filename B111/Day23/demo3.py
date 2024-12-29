def m1(i):
    if i>0:
        print(i)
        i = i - 1
        m1(i)

m1(10)