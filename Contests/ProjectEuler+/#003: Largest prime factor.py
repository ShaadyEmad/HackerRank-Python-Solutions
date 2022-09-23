import math


def largest_prime_factor(n):
    largest_prime = -1

    # handle even integers
    while n % 2 == 0:
        largest_prime = 2
        n = n/2

    # handle odd integers
    while n % 3 == 0:
        largest_prime = 3
        n = n/3

    # handle integer that isn't even or odd
    for i in range(5,int(math.sqrt(n))+1,6):
        while n % i == 0:
            largest_prime = i
            n = n/i

        while n % (i+2) == 0:
            largest_prime = i+2
            n = n/(i+2)

    # handle if n is prime number
    if n > 4:
        largest_prime = n

    return int(largest_prime)


t = int(input())
for case in range(t):
    n = int(input())
    print(largest_prime_factor(n))
