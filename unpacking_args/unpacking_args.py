def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

# Unpacking args
def add(x, y, z):
    return x + y + z

# Unpacking keyword args
def unpacking_keyword_args(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])

print(multiply(1, 5 ,7))

nums = [5, 8, 9]

print(add(*nums))

unpacking_keyword_args(name="Kartick", age=25)
