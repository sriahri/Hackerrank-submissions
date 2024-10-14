#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a=len(s)
    x=''
    if s=='a':
        return n
    elif s.count('a')==0:
        return 0
    else:
        return s.count('a')*(n//len(s))+s[:(n%len(s))].count('a')
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
