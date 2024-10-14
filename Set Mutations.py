n=int(input())
s=set(map(int,input().split()))
n1=int(input())
for i in range(n1):
    l=list(input().split())
    b=int(l[1])
    s1=set(map(int,input().split()))
    if l[0]=='intersection_update':
        s.intersection_update(s1)
    elif l[0]=='update':
        s.update(s1)
    elif l[0]=='symmetric_difference_update':
        s.symmetric_difference_update(s1)
    elif l[0]=='difference_update':
        s.difference_update(s1)
print(sum(s))
