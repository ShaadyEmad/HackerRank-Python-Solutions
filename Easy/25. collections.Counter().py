from collections import Counter

# get the number of shoes
shoes = int(input())

# get all the stock details in the shop.
# split() ------> Split a string into a list where each word is a list item
# Counter ------> is a container that will hold the count of each of the elements present in the container.
# The counter is a sub-class available inside the dictionary class.
stock = Counter(map(int,input().split()))

# get the number of customers
customers = int(input())

income = 0

# for loop to take Purchases equal to number of customers
for i in range(customers):
    # to determine that the first number is the size of shoes and the second number is the cost
    size, cost = map(int,input().split())
    # check if this size available or not
    if (size in stock) and (stock[size]>0):
        # to reduce the number of this size
        stock[size] -= 1
        # to increase the income
        income += cost

print(income)
