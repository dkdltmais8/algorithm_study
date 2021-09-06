def bfs():
    while Q:
        start = Q.pop(0)
        for i in range(V+1):
            if node[start][i] and not visited[i]:
                visited[i] = visited[start] + 1
                if i == g:
                    return visited[g]
                else:
                    Q.append(i)
    return 0
for tc in range(1, int(input())+1):
    V, E  = map(int,input().split())
    node = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        node[u][v] = 1
        node[v][u] = 1
    s, g = map(int,input().split())
    G = [[] for _ in range(V+1)]
    Q = [s]
    visited = [0]*(V+1)
    print("#{} {}".format(tc, bfs()))


