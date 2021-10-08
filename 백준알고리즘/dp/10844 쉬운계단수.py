n = int(input())
dp = [[0 for _ in range(10)] for i in range(101)]
for i in range(1,10):
    dp[1][i] = 1
for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n]) % 1000000000)
#뒷자리가 1이 오려면 그전에 가 0 혹은 2가 와야 하므로
# 그전의 앞, 뒤 값을 누적시켜서 값을 구하고 뒷자리가 0이 오려면
# 무조건 앞에는 1이어야 하고 뒷자리가 9가 되려면 앞자리가 무조건
# 8이어야 하기 때문에 누적값을 구해서 계산한다.