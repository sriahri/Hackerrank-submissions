#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def intersect(a,b):
    return a&b
def gemstones(arr):
    l=[]
    for i in arr:
        l.append((set(i)))
    x=l[0]
    for i in range(1,len(l)):
        if not intersect(x,l[i]):
            return 0
        else:
            x=intersect(x,l[i])
    return len(x)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
