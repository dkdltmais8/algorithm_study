n,m = map(int,input().split())
price = [list(map(int,input().split())) for _ in range(m)]
cheapone = sorted(price,key=lambda x:x[1])
cheapsix = sorted(price,key=lambda x:x[0])
cheapone = cheapone[0][1]
cheapsix = cheapsix[0][0]
r = 0
for i in range(n,n+6):
    if i%6 == 0:
        r= i
        break
dp = [0]*r
tot = cheapone
if n>6:
    for i in range(5):
        dp[i] = tot
        tot += cheapone
    dp[5] = min(cheapsix,dp[4]+cheapone)
    for i in range(6,r):
        dp[i] = min(dp[i-1]+cheapone,dp[i-6]+cheapsix)
    print(min(dp[n - 1:r]))
else:
    dp[n-1] = min(cheapone*n,cheapsix)
    print(dp[n-1])

