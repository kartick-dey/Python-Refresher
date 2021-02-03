def is_prime(num):
    for i in range(2, num):
        if num%2 == 0:
            return False

    return True


def prime_generator(n):
    num = 2

    while n:
        if is_prime(num):
            yield num
            n -= 1
        num += 1

    return

iteratorObj = prime_generator(10)

for el in iteratorObj:
    print(el, end=' ')

def fun():
    print("hello")


var = fun
var()