n=list(map(int,input().split()))
l=list(map(int,input().split()))
s=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if (l[i]+l[j])%n[1]==0:
            s+=1
print(s)
