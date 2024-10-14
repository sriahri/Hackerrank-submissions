#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    s=1
    if n==1:
        print(1)
    else:
        for i in range(1,n+1):
            s*=i
        print(s)


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
