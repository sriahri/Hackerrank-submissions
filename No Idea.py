# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,raw_input().strip().split(' '))
a=map(int,raw_input().strip().split(' '))
s1=map(int,raw_input().strip().split(' '))
s2=map(int,raw_input().strip().split(' '))
s1=set(s1)
s2=set(s2)
ans=0
for i in a:
    if i in s1:
        ans+=1
    elif i in s2:
        ans-=1
print ans