n=int(input())
for i in range(n):
    l=list(map(str,input().split()))
    for i in l[0]:
        print(chr(ord(i)^ord(l[1])),end='')
    print()