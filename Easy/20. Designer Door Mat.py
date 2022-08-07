# to understand this code try to run first half alone first then run the second half alone 

# get the input from user in the same line
N, M = map(int, input().split())

# the first half
for i in range(1, N, 2):
    print((i * ".|.").center(M,"-"))
    
# the middle
print("WELCOME".center(M, "-"))

# the second half
for i in range(N-2, -1, -2):
    print((i * ".|.").center(M, "-"))
