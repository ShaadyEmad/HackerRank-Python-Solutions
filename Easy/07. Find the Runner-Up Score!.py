if __name__ == '__main__':
    # get the value of n from user       example: 5
    n = int(input())
    # get participants' score from user  example: 2 3 6 6 5
    arr = map(int, input().split())
    
    # remove the duplicates items from list using dict.fromkeys()  
    # convert to list using list() function
    # output of this line --------> [2,3,6,5]
    arr = list(dict.fromkeys(arr))
    
    # sort the list from the smallest to the largest
    # output of this line --------> [2,3,5,6]
    number_list = sorted(arr)
    
    # print the second element form the end
    # output of this line --------> 5 
    print(number_list[-2])
