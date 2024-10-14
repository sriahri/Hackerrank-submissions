n=int(input())
l=list(map(str,input().split()))
s=[]
r=[]
for i in range(len(l)):
    x=l[i].split('/')
    s.append(int(x[0])/int(x[1]))
for i in s:
    r.append(i)
s.sort()
for i in range(len(r)):
    if r[i]==s[n-1]:
        print(l[i])
        break

