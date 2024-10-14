n=int(input())
l1=list(map(int,input().split()))
s1=set(l1)
n1=int(input())
l2=list(map(int,input().split()))
s2=set(l2)
s3=s1^s2
print(len(s3))