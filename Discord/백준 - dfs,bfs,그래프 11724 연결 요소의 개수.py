import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def bfs(idx,now):
    visit[now] = idx
    for i in graph[now]:
        if not visit[i]:
            bfs(idx,i)
    return
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    if not visit[i]:
        bfs(i,i)
print(len(set(visit))-1)