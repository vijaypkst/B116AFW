from datetime import datetime
now=datetime.now()

print(now)

a=now.strftime("%Y_%m_%d_%H_%M_%S")
print(a)