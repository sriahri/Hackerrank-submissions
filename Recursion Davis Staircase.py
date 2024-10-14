#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    l=[0]*(n+1)
    l[0]=1
    l[1]=1
    s=0
    for i in range(2,n+1):
        s=0
        if i>=1:
            s+=l[i-1]
        if i>=2:
            s+=l[i-2]
        if i>=3:
            s+=l[i-3]
        l[i]=s
    return (l[-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
