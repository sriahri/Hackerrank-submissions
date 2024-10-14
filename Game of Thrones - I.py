#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the gameOfThrones function below.
def gameOfThrones(s):
    d=Counter(s)
    c=0
    if len(s)==1:
        return 'NO'
    for i in d.keys():
        if d[i]%2!=0:
            c+=1
    if c==1 or c==0:
        return 'YES'
    return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
