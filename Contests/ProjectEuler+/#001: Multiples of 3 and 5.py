# Note that there are common numbers that are multiples of 3 and 5 at the same time, for example 15, 30, etc...

t = int(input())

def solve(n, k):

    m = (n-1) // k  # get the number of natural numbers below n that are multiples of k
    return k * m * (m+1) // 2   # return the sum of natural numbers below n that are multiples of k


for case in range(t):
    n = int(input())

    # get the sum of the numbers that are divisible by 3 and 5
    # then subtract from them the sum of the numbers that are divisible by 15
    sum = solve(n, 3) + solve(n, 5) - solve(n, 15)
    print(sum)
