s=input()
l=s.split(':')
if l[2][2]=='P' and l[0]!='12':
    l[0]=str(12+int(l[0]))
elif l[2][2]=='A' and l[0]=='12':
    l[0]='00'
for i in l[:2]:
    print(i,end=':')
print(l[2][0],end='')
print(l[2][1])
