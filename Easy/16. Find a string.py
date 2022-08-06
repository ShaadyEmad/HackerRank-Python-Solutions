def count_substring(string, sub_string):
    # make variable to find the index
    count =0
    # make for loop starts from 0 and end At the length of input string
    for i in range(0, len(string)):
        # check if string start from (i) and end at (i+lenght of target string) is equal to target string
        if (string[i:i+len(sub_string)]== sub_string):
            # if true increase the count by one
            count = count+1
    return count
        
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    # call the function
    count = count_substring(string, sub_string)
    print(count)
