import numpy as np
l=list(map(int,input().split()))
a=[]
for i in range(l[0]):
    x=list(map(int,input().split()))
    a.append(x)
b=np.array(a)
print(np.transpose(b))
print(b.flatten())

