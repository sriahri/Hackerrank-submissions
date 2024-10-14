#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    c1=0
    c2=0
    arr.sort()
    for i in range(len(arr)-1):
        c1=c1+arr[i]
    for i in range(1,len(arr)):
        c2=c2+arr[i]
    print(c1,end=' ')
    print(c2)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
