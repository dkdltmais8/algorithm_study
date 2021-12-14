def solution(money):
    answer = 0
    ans = []
    d = len(money)
    dp = [0 for _ in range(d)]
    dp[0] = dp[1] = money[0]
    for i in range(2,d-1):
        dp[i] = max(dp[i-1],dp[i-2]+money[i])
    ans.append(dp[-2])

    dp = [0 for _ in range(d)]
    dp[1] = money[1]
    for i in range(2, d):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    ans.append(dp[-1])

    dp = [0 for _ in range(d)]
    for i in range(2, d):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    ans.append(dp[-1])
    return max(answer)
solution([1,2,3,1])