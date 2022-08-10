#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    # make for loop in range of number of words 
    for i in s.split():
        # replace the first letter in word to capitle letter
        s = s.replace(i,i.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
