import heapq
n,m = map(int,input().split())
arr = list(map(int,input().split()))
heapq.heapify(arr)
for i in range(m):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    tot = a+b
    heapq.heappush(arr,tot)
    heapq.heappush(arr,tot)
print(sum(arr))