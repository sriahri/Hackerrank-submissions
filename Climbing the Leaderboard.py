#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    # s=set(scores)
    # l=sorted(list(s),reverse=True)
    # x=[]
    # n=len(l)
    # for i in alice:
    #     low=0
    #     high=n-1
    #     if i in l:
    #         x.append(l.index(i)+1)
    #         continue
    #     while low<=high and l[low]>i:
    #         if l[(low+high)//2]>i:
    #             low=(low+high)//2+1
    #         elif l[(low+high)//2]<i:
    #             high=(low+high)//2-1
    #         else:
    #             break
    #     x.append(low+1)
    # return x
    scores = sorted(list(set(scores)))
    index = 0
    rank_list = []
    n = len(scores)
    for i in alice:
        while (n > index and i >= scores[index]):
            index += 1
        rank_list.append(n+1-index) 
    return rank_list
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
