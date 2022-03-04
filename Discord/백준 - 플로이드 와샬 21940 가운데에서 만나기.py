import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[0 if x == y else float('inf') for y in range(n+1)] for x in range(n+1)]
for _ in range(m):
    s,e,d = map(int,input().split())
    graph[s][e] = min(graph[s][e],d)
#경유 위치
for v in range(1,n+1):
    #출발 위치
    for s in range(1,n+1):
        #도착 위치
        for e in range(1,n+1):
            if graph[s][e]> graph[s][v]+graph[v][e]:
                graph[s][e] = graph[s][v] + graph[v][e]

k = int(input())
arr = list(map(int,input().split()))
min_value = float("inf")
min_list = []
for i in range(1,n+1):
    tot = 0
    for j in arr:
        if graph[j][i] + graph[i][j]>tot:
            tot = graph[j][i] + graph[i][j]
    if tot < min_value:
        min_value = tot
        min_list = [i]
    elif tot == min_value:
        min_list.append(i)
print(*min_list)