from collections import deque
def dfs(idx):
    print(f'{idx}',end=' ')
    visited[idx] = 1
    for i in graph[idx]:
        if visited[i] == 0:
            dfs(i)
def bfs(idx):
    Q=deque([idx])
    visited[idx] = 1
    while Q:
        start = Q.popleft()
        print(start, end=' ')
        for i in graph[start]:
            if visited[i] ==0:
                Q.append(i)
                visited[i] = 1

n,m,v = map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
for i in graph:
    i.sort()
visited = [0] * (n+1)
dfs(v)
print()
visited = [0] * (n+1)
bfs(v)