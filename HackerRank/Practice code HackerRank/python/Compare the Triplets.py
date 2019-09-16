#!/bin/python

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    scoreBoard = [0,0]
    for x,y in zip(a,b):
        if(x>y):
            scoreBoard[0] +=1
        elif(x==y):
            pass
        else:
            scoreBoard[1] +=1

    return scoreBoard

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
