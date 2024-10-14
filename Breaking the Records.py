n=int(input())
x=list(map(int,input().split()))
a=x[0]
b=x[0]
l=0
h=0
for i in range(1,n):
    if x[i]>b:
        h+=1
        b=x[i]
    if x[i]<a:
        l+=1
        a=x[i]
print(h,end=' ')
print(l)
