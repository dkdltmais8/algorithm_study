import heapq
def solution(n, s, a, b, fares):
    #출발 인덱스 노드에서 모든 노드까지 도달하는 데 최소 요금 저장해서 반환
    def move(idx):
        dist = [float('inf')]* (n+1)
        dist[idx] = 0
        Q = []
        heapq.heappush(Q,(0,idx))
        while Q:
            v,d = heapq.heappop(Q)
            if dist[d] < v:
                continue
            for V,D in graph[d]:
                nv = V+v
                if dist[D] > nv:
                    dist[D] = nv
                    heapq.heappush(Q,(nv,D))
        return dist
    answer = float('inf')
    #요금 입력
    graph = [[] for _ in range(n+1)]
    for i in fares:
        graph[i[0]].append([i[2],i[1]])
        graph[i[1]].append([i[2],i[0]])
    # 각 출발 노드에서 최소 요금으로 최신화된 요금표로 저장
    ans = [[]]+[move(i) for i in range(1,n+1)]
    #모든 노드들을 돌면서 출발,A,B까지의 요금이 제일 싼 곳 출력
    for i in range(1,n+1):
        answer = min(ans[i][a]+ans[i][b]+ans[i][s],answer)
    return answer
solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])