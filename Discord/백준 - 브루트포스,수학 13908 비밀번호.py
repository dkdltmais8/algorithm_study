import sys
input = sys.stdin.readline
def factorial(n):
    ans = 1
    for i in range(n,0,-1):
        ans *= i
    return ans
def nCr(n,r):
    ans = factorial(n)//(factorial(n-r)*factorial(r))
    return ans
n,m = map(int,input().split())
cnt = 10
ans = 0
if m:
    lst = list(map(str,input().split()))
for i in range(m+1):
    ans += ((-1)**i)*pow(cnt,n)*nCr(m,i)
    cnt -= 1
print(ans)

