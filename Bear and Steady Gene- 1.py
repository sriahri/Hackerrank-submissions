from collections import Counter 
def findSubString(string, pat):  
    no_of_chars =256
    len1 = len(string)  
    len2 = len(pat) 
    if len2 ==0:
        return 0  
    hash_pat = [0] * no_of_chars 
    hash_str = [0] * no_of_chars    
    for i in range(0, len2):  
        hash_pat[ord(pat[i])] += 1
    start, start_index, min_len = 0, -1,999999
    count = 0   
    for j in range(0, len1):   
        hash_str[ord(string[j])] += 1 
        if (hash_pat[ord(string[j])] != 0 and
            hash_str[ord(string[j])] <= 
            hash_pat[ord(string[j])]):  
            count += 1  
        if count == len2:  
            while (hash_str[ord(string[start])] >  
                   hash_pat[ord(string[start])] or
                   hash_pat[ord(string[start])] == 0):  
                if (hash_str[ord(string[start])] >  
                    hash_pat[ord(string[start])]):  
                    hash_str[ord(string[start])] -= 1
                start += 1
            len_window = j - start + 1
            if min_len > len_window:  
                min_len = len_window  
                start_index = start   
    return string[start_index : start_index + min_len] 
n=int(input())
s=input()
d=Counter(s)
m=0
mn=0
r=n//4
exc=''
for i in d.keys():
    if d[i]>r:
        exc+=i*(d[i]-r)
#print(exc)
if exc=='':
    print(0)
else:
    print(len(findSubString(s,exc)))
'''
def f(s,i):
    p=0
    for j in range(4):
        if s[i]==c[j]:
            p=j
    return p
def ok(x,n):
    flag=False
    for i in range(4):
        if x[i]>n//4:
            return False
    return True
def min(i,j):
    if i<j:
        return i
    else:
        return j
def gene(s):
    x=[0]*4
    k=0
    n=len(s)
    for j in range(len(s)):
        k=f(s,j)
        x[k]+=1
    if ok(x,n):
        return 0
    ans=n
    j=0
    for i in range(len(s)):
        while j<n and not(ok(x,n)):
            x[f(s,j)]-=1
            j+=1
        if ok(x,n):
            ans=min(ans,j-i)
        x[f(s,i)]+=1
    return ans
n = int(input())
st = input()
c=['A','C','T','G']
# initialize counter : overtaken gene number
res=gene(st)
print(res)
'''
