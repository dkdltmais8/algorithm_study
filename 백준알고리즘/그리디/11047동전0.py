n, m = map(int,input().split())
coin = list(int(input()) for _ in range(n))
# print(coin)
ans = 0
for i in range(n-1,-1,-1):
    if m == 0:
        break
    if coin[i] <= m:
        ans += m // coin[i]
        m = m%coin[i]
print(ans)

