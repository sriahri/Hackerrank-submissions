l=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=min(a)
y=max(b)
p=0
m=range(x,y+1)
for j in m:
    for i in a:
        if j%i==0:
            pass
        else:
            break
    else:
        for k in b:
            if k%j==0:
                pass
            else:
                    break
        else:
            p+=1
print(p)

            
