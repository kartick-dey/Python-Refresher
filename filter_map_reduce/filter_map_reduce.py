from functools import reduce

num = [4, 5, 6, 8, 9, 10, 2]

evens = list(filter(lambda n : n%2 == 0, num))

print("Fileter even numbers: ", evens)

doubleOfEvenNumbers = list(map(lambda n: n*2, evens))

print("Doubled of even number: ", doubleOfEvenNumbers)

addAllEvens = reduce(lambda n,m : n+m, doubleOfEvenNumbers)

print("Sum of al doubled even number: ", addAllEvens)