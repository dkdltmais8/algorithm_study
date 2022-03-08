#먼저 도착할 수 있는지. 없으면 gg
#도착 할 수 있다면 2번 도착해보기 ( 돈이 증가하면 무한대 증가가능하므로 GEE)
#2번 도착했을 때 돈이 줄었다면 첫번째 돈이 최대이므로 그 가격 출력
n,s,e,m = map(int,input().split())
graph = [[] for _ in range(n)]
now = 0
for i in range(m):
    S,E,D = map(int,input().split())
    graph[S].append([E,D])
    graph[E].append([S,D])
money = list(map(int,input().split()))
print(graph)