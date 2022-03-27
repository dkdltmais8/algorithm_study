from collections import deque
import sys
def bfs(idx):
    Q = deque()
    Q.append(idx)
    visit[idx] = 0
    while Q:
        now = Q.popleft()
        next = [now-1,now+1]
        if arr[now]:
            next.extend(arr[now])
        for i in next:
            if 1 <= i <= n and visit[i] == -1:
                visit[i] = visit[now]+1
                Q.append(i)
            if i== e:
                return visit[i]

input = sys.stdin.readline
n,m = map(int,input().split())
s,e = map(int,input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
visit = [-1]*(n+1)
ans = bfs(s)
print(ans)