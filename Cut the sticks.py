n=int(input())
l=list(map(int,input().split()))
b=[]
b.append(n)
for i in range(len(set(l))-1):
    c=0
    x=min(l)
    a=l.count(x)
    for j in range(a):
        l.remove(x)
    j=0
    for j in range(len(l)):
        l[j]-=x
        c+=1
    b.append(c)
for i in b:
    print(i)
