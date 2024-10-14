import numpy as np
l=list(map(int,input().split()))
a=[]
for i in range(l[0]+l[1]):
    x=list(map(int,input().split()))
    a.append(x)
print(np.array(a))

