n=int(input())
if n<1918:
    if n%4==0:
        print('12.09.'+str(n))
    else:
        print('13.09.'+str(n))
elif n==1918:
    print('26.09.1918')
else:
    if n%400==0 or n%4==0 and n%100!=0:
        print('12.09.'+str(n))
    else:
        print('13.09.'+str(n))
