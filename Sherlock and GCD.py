#!/bin/python3

import os
import sys
from math import gcd
# Complete the solve function below.
def solve(a):
    g=a[0]
    a.sort(reverse=True)
    for i in range(1,len(a)):
        g=gcd(a[i],g)
    if g==1:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a_count = int(input())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(result + '\n')

    fptr.close()
