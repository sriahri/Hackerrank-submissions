n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
s1=set(l1)
s2=set(l2)
s3=s1^s2
l3=list(s3)
l3.sort()
for i in l3:
    print(i)