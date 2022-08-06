# make function called split_and_join() which have parameter (line)
# paeameter (line) ------> is the input from user 
def split_and_join(line):
    # split(" ") ----> every space it split the string 
    split = line.split(" ")
    # "-".join   ----> it will replace every space with '-'
    # join will also remove the (, [] '') from the list
    return "-".join(split)

if __name__ == '__main__':
    # takes the input from user
    line = input()
    # call the function 
    result = split_and_join(line)
    print(result)
