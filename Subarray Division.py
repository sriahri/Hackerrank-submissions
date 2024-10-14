n=int(input())
l=list(map(int,input().split()))
x=list(map(int,input().split()))
s=0
if len(l)==x[1]:
    if sum(l)==x[0]:
        s=1
else:
    for i in range(len(l)-x[1]+1):
        if sum(l[i:i+x[1]])==x[0]:
            s+=1
print(s)

