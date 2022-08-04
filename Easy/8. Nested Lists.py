if __name__ == '__main__':
    # make two empty lists
    records = []
    scores = []
    
    # loop to take the number of students from user
    for _ in range(int(input())):
        # takes the name from user
        name = input()
        # takes the score from user
        score = float(input())
        # add the name and score in the list
        records += [[name,score]]
        # add the score only in the list
        scores += [score]
    # sort the list from the smallest to the largest and takes the second element (second smallest number)
    second_lowest_grade = sorted(list(set(scores)))[1]
    # make loop which have (a refers to names) (b refers to score) in the records list
    # sorted the recordes list by alphabets
    for a,b in sorted(records): 
        # Print the names of students that have the second lowest grade 
        # by checking if the score of every student equal to second_lowest_grade
        if b==second_lowest_grade:
            print(a)
