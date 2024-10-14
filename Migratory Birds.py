n=int(input())
l=list(map(int,input().split()))
s=set(l)
x=list(s)
y=[]
for i in range(len(x)):
    y.append(l.count(x[i]))
a=y.index(max(y))
print(x[a])

