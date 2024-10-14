#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    x=0
    i=0
    while i<len(c)-2:
        if c[i+2]==0:
            i+=2
        else:
            i+=1
        x+=1
    if i==len(c)-2:
        x+=1
    return x
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
