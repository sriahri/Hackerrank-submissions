#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the isValid function below.
def isValid(s):
    S=s
    d = Counter(S)
    l = list(d.values())
    mini = min(l)
    maxi = max(l)
    s = set(l)
    s = list(s)
    length = len(s)
    if length == 1:
        return 'YES'
    elif length ==2:
        if l.count(maxi) == 1 and maxi-mini ==1:
            return 'YES'
        elif l.count(mini)==1 and mini ==1:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
