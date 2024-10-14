#!/bin/python3

import math
import os
import random
import re
import sys

def solve(n):
    s=0
    while n!=0:
        s+=n%10
        n=n//10
    return s

if __name__ == '__main__':
    n = int(input())
    maxi=0
    for i in range(1,n+1):
        if n%i==0:
            x=solve(i)
            if x>maxi:
                maxi=x
                ans=i
    print(ans)
