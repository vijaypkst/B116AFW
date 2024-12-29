def ispositive(n):
    return n>0

print(ispositive(10))


ispositive=lambda n:n>0
print(ispositive(10))


def iseven(n):
    return n%2==0
print(iseven(10))

iseven=lambda n:n%2==0
print(iseven(10))

def is_starts_with_a(name):
    return name.startswith('A')

print(is_starts_with_a('Akshara'))

is_starts_with_a=lambda name:name.startswith('A')
print(is_starts_with_a('Akshara'))

def is_upper(name):
    return name.isupper()
print(is_upper('BHANU'))

is_upper=lambda name:name.isupper()
print(is_upper('BHANU'))