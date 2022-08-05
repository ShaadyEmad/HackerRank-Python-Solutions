if __name__ == '__main__':
    # get the number of commands
    N = int(input())
    # make empty list
    list = []

    # make for loop to get commands in range N
    for i in range(N):
        # get the command from user
        command = input()
        # check if the command start with 'insert'
        if command.startswith('insert'):
            # get the index
            # split is function using to make list from input
            # we use [1] to get the index
            # we use int() to convert from string to int
            index = int(command.split()[1])
            # we use [1] to get the number
            num = int(command.split()[2])
            # insert the number in the list
            list.insert(index,num)

        # check if the command start with 'remove'
        elif command.startswith('remove'):
            # we use [1] to get the number
            num = int(command.split()[1])
            # Delete the first occurrence of num
            list.remove(num)

        # check if the command start with 'append'
        elif command.startswith('append'):
            # we use [1] to get the number
            num = int(command.split()[1])
            # Insert num at the end of the list
            list.append(num)

        # check if the command is 'sort'
        elif command == 'sort':
            # Sort the list.
            list.sort()

        # check if the command is 'pop'
        elif command == 'pop':
            # Pop the last element from the list.
            list.pop()

        # check if the command is 'reverse'
        elif command == 'reverse':
            # Reverse the list.
            list.reverse()

        # check if the command is 'print'
        elif command == 'print':
            print(list)
