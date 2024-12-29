def m1(i):
    if i<=0:
        print("end")
    else:

        m1(i-1)   # fn will call and print until i =0
        print(i)


m1(10)