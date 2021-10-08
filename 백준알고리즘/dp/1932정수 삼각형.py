n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = arr
for i in range(1,n):
    for j in range(len(arr[i])):
        #바로 위의 숫자를 더함
        if j == 0:
            dp[i][j] += dp[i-1][j]
        #바로 위의 숫자를 더함
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        #사이의 숫자는 위의 수를 비교해 큰 쪽에다가 더해줌
        else:
            dp[i][j] += max(dp[i-1][j],dp[i-1][j-1])
print(max(dp[n-1]))

##밑을 기준으로 위에서 어떤걸 선택할지 정하는 방식으로 생각하기
