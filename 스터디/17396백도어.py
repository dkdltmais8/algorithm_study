import heapq,sys
INF = sys.maxsize
input = sys.stdin.readline
def dijkstra(start):
    Q = []
    #위치와 시간을 초기화
    heapq.heappush(Q,(start,0))
    time[start] = 0
    while Q:
        #현재위치와 시간
        idx,t = heapq.heappop(Q)
        #현재 시간이 time[idx]보다 크면 가망 없는놈이라 실행 안함
        if time[idx] < t:
            continue
        for i,T in graph[idx]:
            #원래 시간과 도착한 곳의 시간을 더해서 가지고있음
            tot = t+T
            #만약 총 시간이 time[i]저장된 시간보다 작고 갈 수 있는 공간이라면 time[i]를 tot으로 넣고
            # 그 위치를 Q에 넣음
            if tot < time[i] and sight[i] == 0:
                time[i] = tot
                heapq.heappush(Q,(i,tot))

n,m = map(int,input().split())
sight = list(map(int,input().split()))
#어차피 마지막은 가야하므로 마지막은 갈 수 있게만들고 사이에 있는 1을 기점으로 판단하기
sight[-1] = 0
#갈 수 있는 루트 만들기
graph = [[] for _ in range(n+1)]
#시간 비교하는 리스트 만들기
time = [INF]*(n+1)
for i in range(m):
    v,e,t = map(int,input().split())
    graph[v].append((e,t))
    graph[e].append((v,t))
# print(n,m)
# print(sight)
# print(graph)
dijkstra(0)
# print(time)
# print(graph)
#마지막에 도착 했을 때 시간이 초기설정값이 아니라면 출력하고 맞다면 갈 수 없다는 것이기 때문에 -1리턴
print(time[n-1] if time[n-1] != sys.maxsize else -1)


################################################
# 다익스트라 알고리즘 => 최단 경로 트리(가중치 이용)
#
# - 가중치의 합이 제일 적게 끝 노드에 도착
# - heapq, heappush, heappop 이용
# - 처음에 갈 수 있는 경로가 들어있는 List 만들어주기.(Graph)
# - 사용하는 함수만 다르고 BFS와 비슷함.(append 대신 heapq.heappush,      pop 대신 heapq.heappop)