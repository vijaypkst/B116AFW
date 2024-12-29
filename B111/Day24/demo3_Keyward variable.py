def f1(city=None,area=None): #keyword argument
    print('city is',city,'Area is',area)


f1() #None None

f1('Bengaluru') #Bengaluru None

f1('Bengaluru','MG Road')

f1(city='Delhi',area='Hari Nagar')

f1('Hari Nagar','Delhi')

f1(area='Hari Nagar',city='Delhi')

f1(area='Hari Nagar')
