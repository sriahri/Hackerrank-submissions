#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    c1=0
    c2=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i==j:
                c1=c1+arr[i][j]
                
            if i+j==(n-1):
                c2=c2+arr[i][j]
    return abs(c1-c2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
