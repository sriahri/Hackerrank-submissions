#!/bin/python3

import os
import sys

#
# Complete the closestNumber function below.
#
def closestNumber(a, b, x):
    #
    # Write your code here.
    #
    p=a**b
    y=p//x
    c=x*y
    d=x*y+x
    if abs(c-p)<abs(d-p) or abs(c-p)==abs(d-p):
        return int(c)
    return int(d)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abx = input().split()

        a = int(abx[0])

        b = int(abx[1])

        x = int(abx[2])

        result = closestNumber(a, b, x)

        fptr.write(str(result) + '\n')

    fptr.close()
