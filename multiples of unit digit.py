n=int(input())
s=n%10
x=0
i=1
while x<n:
    if s==0:
        s=10
    print(s*i,end=' ')
    i+=1
    x=s*i
