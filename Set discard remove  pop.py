n=int(input())
l=list(map(int,input().split()))
s=set(l)
n2= int(input())
for i in range(n2):
    l=list(input().split())
    if l[0]=='remove':
        s.remove(int(l[1]))
    elif l[0]=='discard':
        s.discard(int(l[1]))
    elif l[0]=='pop':
        s.pop()
print(sum(s))
        