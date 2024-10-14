from itertools import *
l=list(input().split())
x=list(permutations(l[0],int(l[1])))
x.sort()
for i in range(len(x)):
    for j in range(int(l[1])):
        print(x[i][j],end='')
    print()
    
        