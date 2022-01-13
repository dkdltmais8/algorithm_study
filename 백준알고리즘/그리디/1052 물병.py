n, m = map(int,input().split())
ans = 0
while bin(n).count('1')>m:
    now = bin(n)[::-1].index('1')
    ans += 2**now
    n += 2**now
print(ans)