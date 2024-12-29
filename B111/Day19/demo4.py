#can we use break and continue in while loop also?

i=1
while i<=10:
    if i>5:
        break
    print(i)
    i+=1

print('-'*7)
i=0
while i<=10:
    i += 1
    if i>=5 and i<=8:
        continue
    print(i)

