import heapq
for _ in range(int(input())):
    n = int(input())
    arr= list(map(int,input().split()))
    heapq.heapify(arr)
    tot = 0
    while len(arr)>1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        heapq.heappush(arr,a+b)
        tot += a+b
    print(tot)