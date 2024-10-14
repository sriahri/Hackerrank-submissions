n=int(input())
l=list(map(int,input().split()))
s=set(l)
x=list(s)
y=[]
a=0
for i in x:
    y.append(l.count(i))
for i in y:
    a+=i//2
print(a)
