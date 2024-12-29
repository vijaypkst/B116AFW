def function1():
    print('Hi')

def function2(f):   #it is taking another function as argument --> higher order function
    f()

function1()
function2(function1)
