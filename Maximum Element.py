# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
x=[]
m=0
for _ in range(t):
    l=list(map(int,input().split()))
    if len(l)==2:
        x.append(l[1])
        m=max(l[1],m)
    else:
        if l[0]==2:
            if len(x)!=0:
                temp=x.pop()
            if temp==m:
                if len(x)!=0:
                    m=max(x)
                else:
                    m=0
        else:
            if len(x)!=0:
                print(m)
