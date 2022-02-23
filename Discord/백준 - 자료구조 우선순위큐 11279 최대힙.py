import heapq,sys
input = sys.stdin.readline
Q = []
tc = int(input())
for _ in range(tc):
    n = int(input())
    if n == 0:
        if Q:
            print(heapq.heappop(Q)[1])
        else:
            print(0)
    elif n/1 == n:
        heapq.heappush(Q,(-n,n))
