n=int(input())
for i in range(n):
    x=int(input())
    s=set(map(int,input().split()))
    y=int(input())
    s1=set(map(int,input().split()))
    print(s<=s1)