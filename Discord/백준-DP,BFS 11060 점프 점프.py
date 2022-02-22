#dp
n = int(input())
arr = list(map(int,input().split()))
dp = [n+1]*(n)
dp[0] = 0
for i in range(n):
    for j in range(1,arr[i]+1):
        if i+j>=n:
            break
        dp[i+j] = min(dp[i+j],dp[i]+1)
print(dp[n-1] if dp[n-1]!=n+1 else -1)

# bfs
from collections import deque
import sys
n = int(input())
arr = list(map(int,input().split()))
Q = deque([(0,arr[0])])
visit = [0]*n
if n == 1:
    print(0)
    sys.exit()
while Q:
    idx,move = Q.popleft()
    for i in range(1,move+1):
        if idx+i>=n or visit[idx+i]:
            continue
        visit[idx+i] = visit[idx]+1
        Q.append((idx+i,arr[idx+i]))
print(visit[n-1] if visit[n-1] else -1)