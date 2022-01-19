import heapq
n = int(input())
Q = []
for i in range(n):
    s,e = map(int,input().split())
    heapq.heappush(Q,(s,e))
room = []
for i in range(n):
    s,e = heapq.heappop(Q)
    if not room:
        heapq.heappush(room,(e,s))
        continue
    be,bs = heapq.heappop(room)
    if be>s:
        heapq.heappush(room,(be,bs))
    heapq.heappush(room,(e,s))
print(len(room))