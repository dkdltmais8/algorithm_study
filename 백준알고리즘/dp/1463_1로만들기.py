n = int(input())
dp = [0] * (n+1)
#1을 만드는 문제이기 때문에 1인덱스에 0 을 넣고 각 인덱스에 맞는 횟수를 넣음
for i in range(2, n + 1):
    #1을 빼니까 전의 수보다 1씩 큼
    dp[i] = dp[i - 1] + 1
    #2의 배수이고 그 전의 2의 배수보다 1이상 큰 수는 잘못된 방식이므로 +1으로 바꿔줌
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
    # 3의 배수이고 그 전의 3의 배수보다 1이상 큰 수는 잘못된 방식이므로 +1으로 바꿔줌
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1

print(dp[n])