import heapq,sys
input = sys.stdin.readline
def dijkstra():
    Q = []
    tot = float("inf")
    for i in range(1,v+1):
        if i in M or i in S:
            continue


v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
for i in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))
m,x = map(int,input().split())
M = list(map(int,input().split()))
s,y = map(int,input().split())
S = list(map(int,input().split()))
print(graph,M,S,x,y)
dijkstra()