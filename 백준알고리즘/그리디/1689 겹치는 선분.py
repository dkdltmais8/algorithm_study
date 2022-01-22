import heapq,sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[0],x[1]))
Q = []
heapq.heappush(Q,arr[0][1])
cnt = 1
for i in arr[1:]:
    while Q and Q[0]<=i[0]:
        heapq.heappop(Q)
    heapq.heappush(Q,i[1])
    cnt = max(cnt,len(Q))
print(cnt)
