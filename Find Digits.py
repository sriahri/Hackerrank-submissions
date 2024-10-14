#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the findDigits function below.
def findDigits(n):
    c=0
    x=n
    while x!=0:
        s=x%10
        if s==0:
            pass
        elif n%s==0:
            c+=1
        x=x//10
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
