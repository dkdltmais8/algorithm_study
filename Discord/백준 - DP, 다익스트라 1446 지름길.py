n,d = map(int,input().split())
dp = [i for i in range(d+1)]
Q = []
for i in range(n):
    a,b,c = map(int,input().split())
    Q.append((a,b,c))
Q.sort(key=lambda x:(x[0],x[1],x[2]))
for i in Q:
    s,e,w = i
    if e<=d:
        #현재 이동 거리는 출발점에서 지름길 거리, 기존의 거리 중에 작은것
        dp[e] = min(dp[s]+w,dp[e])
    for j in range(s,d+1):
        dp[j] = min(dp[j-1]+1,dp[j])
print(dp[d])