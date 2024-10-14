l=list(map(int,input().split()))
b=list(map(int,input().split()))
m=list(map(int,input().split()))
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=range(l[0],(l[1]+1))
a=0
o=0
for i in x:
    if (i+b[0]) in z:
        a+=1
for i in y:
    if (i+b[1])in z:
        o+=1
print(a)
print(o)

    
