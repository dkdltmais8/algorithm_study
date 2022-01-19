import heapq
import sys
input = sys.stdin.readline
n = int(input())
c = []
for _ in range(n):
    i,s,e = map(int,input().split())
    heapq.heappush(c,(s,e,i))
room = []
for i in range(n):
    s,e,i = heapq.heappop(c)
    if not room:
        heapq.heappush(room,(e,s,i))
        continue
    be,bs,bi = heapq.heappop(room)
    if be>s:
        heapq.heappush(room,(be,bs,bi))
    heapq.heappush(room,(e,s,i))
print(len(room))