from math import factorial
def C(n, r):
    ans = factorial(n) / (factorial(r) * factorial(n-r))
    return ans

def solve(x, y, k):
    ans = ""
    while k > 0:
        if k < C(x+y-1, y):
            ans += "H"
            x -= 1
        else:
            ans += "V"
            k -= C(x+y-1, y)
            y -= 1
    ans += x * "H"
    ans += y * "V"
    return ans
for _ in range(int(input())):
    x,y,k = map(int,input().split())
    print(solve(x,y,k))
