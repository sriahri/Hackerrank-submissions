n=int(input())
l=list(map(int,input().split()))
x=[]
res=len(l)
l.append(0)
for i in range(len(l)):
    li=i
    while len(x)>0 and x[-1][0]>=l[i]:
        la=x.pop()
        li=la[1]
        res=max(res,l[i]*(i + 1 - la[1]))
        res=max(res,la[0]*(i - la[1]))
    x.append((l[i],li))
print(res)