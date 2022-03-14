for _ in range(int(input())):
    n = int(input())
    case = list(map(int,input().split()))
    money = int(input())
    dp = [0 for _ in range(money+1)]
    dp[0] = 1
    for i in case:
        for j in range(1,money+1):
            if j-i>=0:
                dp[j] += dp[j-i]
    print(dp[-1])