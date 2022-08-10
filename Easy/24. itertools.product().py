# input() ------> get the numbers from user
# split() ------> Split a string into a list where each word is a list item:
A = input().split()
B = input().split()

# make loop wich acces each item in A 
for i in A:
    # make loop wich acces each item in A 
    for y in B:
        # end = ' ' -----> use to print in the same line
        print(f"({i}, {y})" ,end = ' ')
