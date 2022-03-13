N, H = map(int,input().split())
#0부터 시작하는 맵으로 변형시키기
if N>H:
    a,b = 0,N-H
else:
    a,b = 0,H-N
#맵의 크기에 맞는 dp
dp = [[0]*(b+1) for _ in range(b+1)]
#맵을 돌면서 초기 테두리에 1씩 채워주기
#i가 0일 때는 j가 다 커지므로 윗변은 무시
for i in range(b+1):
    for j in range(b+1):
        if i<j:continue
        if i == b:
            dp[i][j] = 1
        elif j == 0:
            dp[i][j] = 1
#x축 전과 y축 전의 방법 더해주기
for i in range(a,b+1):
    for j in range(a,b+1):
        if i<j:
            continue
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
#마지막 방법의 수와 처음 1빼주기
print(dp[-1][-1]-1)
