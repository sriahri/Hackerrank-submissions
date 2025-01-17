#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the canConstruct function below.
def canConstruct(a):
    s=''
    for i in a:
        s+=str(i)
    x=int(s)
    if x%3==0:
        return 'Yes'
    return 'No'
    # Return "Yes" or "No" denoting whether you can construct the required number.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        result = canConstruct(a)

        fptr.write(result + '\n')

    fptr.close()
