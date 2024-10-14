#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    l=[]
    x=len(h)
    h.append(0)
    for i in range(len(h)):
        li=i
        while len(l)>0 and l[-1][0]>=h[i]:
            last=l.pop()
            li=last[1]
            x=max(x,h[i]*(i + 1 - last[1]))
            x=max(x,last[0]*(i - last[1]))
        l.append((h[i],li))
    
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
