import heapq
def solution(N, road, K):
    def dijkstra(d,info):
        Q = []
        heapq.heappush(Q,[0,1])
        while Q:
            dist,node = heapq.heappop(Q)
            for d,n in info[node]:
                if dist+d < dis[n]:
                    dis[n] = dist+d
                    heapq.heappush(Q,[dist+d,n])
    inf = float("inf")
    #거리
    dis = [inf]*(N+1)
    dis[1] = 0
    #연결 지점 정보
    info = [[] for _ in range(N+1)]
    #최소한의 거리를 찾기 위해 거리부터 리스트에 넣어준다.
    for i in road:
        info[i[0]].append([i[2],i[1]])
        info[i[1]].append([i[2],i[0]])
    dijkstra(dis,info)
    return len([i for i in dis if i<=K])
solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)