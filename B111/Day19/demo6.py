#add 2 given numbers until user says STOP

while True:
  n1=int(input('please enter a number'))
  n2=int(input('please enter another number'))
  sum=n1+n2
  print('Sum is:',sum)
  stop=input('Do you want to stop? yes/no')
  if stop=='yes':
      print('Thank You')
      break