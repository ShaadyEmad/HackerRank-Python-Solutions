if __name__ == '__main__':
    # get the value of n from user
    n = int(input())
    # make empty dictionary
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        # put every score with its name in the dictionary
        student_marks[name] = scores
    # gets the name for which we will find the percentage of
    query_name = input()
    # calculate the percentage by ( sum / the number of numbers )
    # we use variable query_name to find the percentage for the specific name
    percentage = sum(student_marks[query_name])/len((student_marks[query_name]))
    # we use "%.2f"   to get two numbers after comma (ex:56.00)
    print("%.2f" % percentage)
