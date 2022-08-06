# make function called mutate_string()   takes 3 parameters (string, position, character)
def mutate_string(string, position, character):
    # convert the input to list (to be able to access the specific index)
    string_list = list(string)
    # access the specific index and replace it by (character)
    string_list[position] = character
    # "".join   ----> it will replace every space with ''
    # join will also remove the (, [] '') from the list
    string = ''.join(string_list)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    # call the function
    s_new = mutate_string(s, int(i), c)
    print(s_new)
