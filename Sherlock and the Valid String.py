#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the isValid function below.
def isValid(s):
    if len(s)==1:
        return "YES"
    x=Counter(s)
    l=[]
    for i in x.keys():
        l.append(x[i])
    a=list(set(l))
    print(a)
    if len(a)==1:
        return "YES"
    elif len(a)==2:
        m=l.count(max(a))
        n=l.count(min(a))
        if m==1 and max(a)-min(a)==1:
            return 'YES'
        elif n==1 and min(a)==1:
            return 'YES'
    return 'NO'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
