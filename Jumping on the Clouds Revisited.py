#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    x=0
    i=0
    while 1:
        if k==len(c):
            return 97
        if c[i+k]==1:
            x+=2
        x+=1
        i+=k 
        if (i+k)>=len(c):
            if c[0]==1:
                x+=2
            x+=1
            break
    return 100-x


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
