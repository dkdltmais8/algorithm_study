def dfs(idx):
    global cnt
    visited[idx] = 1
    cnt +=1
    for i in graph[idx]:
        if visited[i] == 0:
            dfs(i)
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
visited=[0] * (n+1)
cnt = 0
dfs(1)
print(cnt)