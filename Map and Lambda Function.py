cube = lambda x:x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    l=[]
    i=0
    if n==0:
        pass
    elif n==1:
        l.append(0)
    else:
        a=0
        b=1
        l.append(a)
        l.append(b)
        while i<n-2:
            c=a+b
            a=b
            b=c
            l.append(c)
            i+=1
    return l
