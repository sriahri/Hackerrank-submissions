n=list(map(int,input().split()))
l=list(map(int,input().split()))
b=int(input())
if n[1]!=0:
    s=l[:n[1]]+l[n[1]+1:]
    x=sum(s)
    a=x//2
    if b==a:
        print('Bon Appetit')
    else:
        print(b-a)
else:
    print('Bon Appetit')
