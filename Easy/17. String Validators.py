if __name__ == '__main__':
    s = input()
    # any() -----> use to check if any of the items are True
    # using for loop is for access every element in the input
    
    # isalnum() -----> checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
    print(any(i.isalnum() for i in s) )
    
    # str.isalpha() -----> checks if all the characters of a string are alphabetical (a-z and A-Z).
    print(any(i.isalpha() for i in s) )
    
    # str.isdigit() -----> This method checks if all the characters of a string are digits (0-9).
    print(any(i.isdigit() for i in s) )
    
    # str.islower() -----> This method checks if all the characters of a string are lowercase characters (a-z).
    print(any(i.islower() for i in s) )
    
    # str.isupper() -----> This method checks if all the characters of a string are uppercase characters (A-Z).
    print(any(i.isupper() for i in s) )
