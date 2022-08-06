# make function called print_full_name()  which take two parameter (first, last)
def print_full_name(first, last):
    print(f"Hello {first_name} {last_name}! You just delved into python.")

if __name__ == '__main__':
    # gets the first name from user
    first_name = input()
    # gets the last name from user
    last_name = input()
    # call the function print_full_name()
    print_full_name(first_name, last_name)
