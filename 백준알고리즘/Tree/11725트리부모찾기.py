import sys
sys.setrecursionlimit(10**5)

def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 1:
            pass
        else:
            visited[i] = 1
            parent[i] = x
            dfs(i)
N = int(input())
graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)
visited = [0] * (N+1)
for _ in range(N-1):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
dfs(1)
for i in range(2,N+1):
    print(parent[i])
