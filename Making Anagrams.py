#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    d1=Counter(s1)
    d2=Counter(s2)
    c=0
    for i in d1.keys():
        if i not in d2:
            c+=d1[i]
        else:
            c+=abs(d1[i]-d2[i])
    for i in d2.keys():
        if i not in d1:
            c+=d2[i]
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
