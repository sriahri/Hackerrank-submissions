#!/bin/python3

import math
import os
import random
import re
import sys
x=[]
# Complete the permutationEquation function below.
def permutationEquation(p):
    for i in range(1,n+1):
        a=p.index(i)+1
        x.append(p.index(a)+1)
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
