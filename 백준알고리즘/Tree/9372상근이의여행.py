###문제 탓######
for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    for _ in range(m):
        s,e = map(int,input().split())
    print(n-1)



#####정상적인 풀이###########

def dfs(node, cnt):
    visit[node] = 1
    for n in graph[node]:
        if visit[n] == 0:
            cnt = dfs(n, cnt+1)
    return cnt

for _ in range(int(input())):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visit = [0]*(N+1)
    visit[1] = 0
    cnt = dfs(1, 0)
    print(cnt)