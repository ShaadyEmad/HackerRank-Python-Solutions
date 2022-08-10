def print_formatted(number):
    # the ket poit here to find the type of number that will take biggest width -----> definitely its binary
    # so we convert the input to binary and get its length
    # we subtract (2) from the length to make one space between binary and hexadecimal
    width = len(bin(number)) - 2
    
    for i in range(1,number+1):
        # convert i to string to be able to print it
        # rjsut(width,' ') -----> to make (width) of ' ' before every number 
        # we use end=" " to remain in the same line
        print(str(i).rjust(width,' '),end=" ")
        # the different here is we except the first 2 element of Octal and Hexadecimal and Binary from being printed because we do not need them to represent any type of them
        print(oct(i)[2:].rjust(width,' '),end=" ")
        print((hex(i)[2:].upper()).rjust(width,' '),end=" ")
        print(bin(i)[2:].rjust(width,' '),end=" ")
        # to move to next line
        print(" ")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
