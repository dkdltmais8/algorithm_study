def get(s):
    if s =='B':
        return 'J'
    elif s == "O":
        return "B"
    elif s == "J":
        return "O"

n = int(input())
p = input()
dp = [float('inf')]*n
dp[0] = 0
for i in range(1,n):
    prev = get(p[i])
    for j in range(i):
        if p[j] == prev:
            dp[i] = min(dp[i],dp[j]+(i-j)**2)
print(dp[-1] if dp[-1]!=float('inf') else -1)


