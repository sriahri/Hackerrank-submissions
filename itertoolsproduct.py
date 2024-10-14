from itertools import *
a=set(map(int,input().split()))
b=set(map(int,input().split()))
c=tuple(product(a,b))
for i in c:
    print(i,end=' ')