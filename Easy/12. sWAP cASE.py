# make function called swap_case()  which take parameter s
# parameter s ----> is the input from user
def swap_case(s):
    # we will use swapcase() function 
    return s.swapcase()

if __name__ == '__main__':
    # get the input from user
    s = input()
    # call the function swap_case()
    result = swap_case(s)
    # print the result
    print(result)
