#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    x=list(set(a))
    x.sort()
    max=0
    l=0
    print(x)
    if a.count(x[0])==len(a):
        return len(a)
    for i in range(1,len(x)):
        if x[i]-x[i-1]<=1:
            l=a.count(x[i-1])+a.count(x[i])
        if a.count(x[i-1])>max:
            max=a.count(x[i-1])
        if max<l:
            max=l
    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
