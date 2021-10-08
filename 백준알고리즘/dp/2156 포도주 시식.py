n = int(input())
arr = [int(input()) for i in range(n)]
arr.insert(0,0)
dp = [0]
dp.append(arr[1])
if n >= 2:
    dp.append(arr[1]+arr[2])
for i in range(3,n+1):
    #지금 포도주를 무시하는 경우(다음 것을 먹을 경우)
    #지금까지 최대의 합 = dp[i-1]
    #지금 포도주를 먹고 전 포도주도 먹은 경우 (전전을 건너 뛰고 전, 지금의 합)
    #전전전의 최대 = dp[i-3] + 전과 현재의 값 = arr[i-1] + arr[i] -> dp[i-3] + arr[i-1]이 dp[i-1]이 아닐 수 있기
    #때문에 dp[i-1]로 쓰면 안되고 dp[i-3]에 그냥 값들을 더해줘야 함
    #지금 포도주를 먹고 전 포도주는 먹지 않은 경우 (전전전과 전전을 먹고 전을 건너뛰고 지금것을 마실 때)
    #전전까지 최대의 합 = dp[i-2] + 현재 arr[i]
    dp.append(max(dp[i-1],dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i]))

print(dp[n-1])
