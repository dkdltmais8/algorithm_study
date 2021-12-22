import heapq
n = int(input())
study = [list(map(int,input().split())) for _ in range(n)]
study.sort(key= lambda x:x[0])
room = []
heapq.heappush(room,study[0][1])
for i in range(1,n):
    if room[0] > study[i][0]:
        heapq.heappush(room,study[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, study[i][1])
print(len(room))
