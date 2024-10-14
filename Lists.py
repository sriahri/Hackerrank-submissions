n=int(input())
l1=[]
for i in range(n):
    l2=list(input().split())
    if l2[0]=='insert':
        l1.insert(int(l2[1]),int(l2[2]))
    elif l2[0]=='print':
        print(l1)
    elif l2[0]=='remove':
        l1.remove(int(l2[1]))
    elif l2[0]=='append':
        l1.append(int(l2[1]))
    elif l2[0]=='sort':
        l1.sort()
    elif l2[0]=='pop':
        l1.pop()
    elif l2[0]=='reverse':
        l1.reverse()
    