n = int(input())
road = list(map(int,input().split()))
start = road[0]
tot = 0
ans = []
for i in range(1,n):
    if road[i] - start > 0:
        tot += road[i] - start
        start = road[i]
    elif road[i] == start or road[i] < start:
        ans.append(tot)
        start = road[i]
        tot = 0
ans.append(tot)
if len(ans) == 0:
    print(0)
else:
    print(max(ans))