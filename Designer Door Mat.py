x=list(map(int,input().split()))
l=[]
for i in range(1,x[0]//2+1):
    p=x[0]*3
    o=((i*2)-1)
    q=((i*2)-1)*3
    r=(p-q)//2
    print('-'*r,end='')
    print('.|.'*o,end='')
    print('-'*r)
print('-'*((p-7)//2),end='')
print('WELCOME',end='')
print('-'*((p-7)//2))
for i in range(1,x[0]//2+1):
    l.append(i)
for i in l[::-1]:
    p=x[0]*3
    o=((i*2)-1)
    q=((i*2)-1)*3
    r=(p-q)//2
    print('-'*r,end='')
    print('.|.'*o,end='')
    print('-'*r)


