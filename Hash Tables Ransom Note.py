#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    d1=Counter(magazine)
    d2=Counter(note)
    for i in d2.keys():
        if d2[i]>d1[i]:
            print('No')
            break
    else:
        print('Yes')
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
