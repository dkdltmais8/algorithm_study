import heapq
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
heapq.heapify(arr)
tot = 0
for i in range(n-1):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    heapq.heappush(arr,a+b)
    tot += a+b
print(tot)