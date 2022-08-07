import textwrap

# make function called warp() take 2 parameter (string, max_width)
def wrap(string, max_width):
    # make for loop starts from (0) and end in (length of string) and increase by (max_width)
    for i in range(0, len(string)+1, max_width ):
        # get the result with specific (max_width)
        s = string[i:i+max_width]
        # make condition that if the result length equal to (max_width) ----> print the result
        if len(s) == max_width:
            print(s)
        # else means that it is the last result in the string so we will return it
        else :
            return s


if __name__ == '__main__':
    # get the (string) and (max width) from user
    string, max_width = input(), int(input())
    # call the function
    result = wrap(string, max_width)
    print(result)
