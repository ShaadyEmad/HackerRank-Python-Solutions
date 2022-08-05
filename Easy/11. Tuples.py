if __name__ == '__main__':
    # get number of integers from user
    n = int(input())
    # make list of integers
    integer_list = map(int, input().split())
    # convert list to tuple
    tuple = tuple(integer_list)
    # print hash using hash() function 
    print(hash(tuple))
