# Enter your code here. Read input from STDIN. Print output to STDOUt
from calendar import*
l=list(map(int,input().split()))
x=(weekday(l[2],l[0],l[1]))
if x==6:
    print('SUNDAY')
elif x==0:
    print('MONDAY')
elif x==1:
    print('TUESDAY')
elif x==2:
    print('WEDNESDAY')
elif x==3:
    print('THURSDAY')
elif x==4:
    print('FRIDAY')
else:
    print('SATURDAY')