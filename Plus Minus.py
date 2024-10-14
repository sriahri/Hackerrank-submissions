#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    c1=0
    c2=0
    c3=0
    for i in arr:
        if i<0:
            c2=c2+1
        elif i>0:
            c1=c1+1
        elif i==0:
            c3=c3+1
    print(c1/len(arr))
    print(c2/len(arr))
    print(c3/len(arr))

        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
