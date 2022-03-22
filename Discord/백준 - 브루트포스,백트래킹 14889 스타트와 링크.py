from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = float('inf')
team = []
for i in list(combinations(range(1,n+1),n//2)):
    team.append(i)
for i in team:
    team_b = []
    for j in i:
        team_b.append(n-j+1)
    cnt_a,cnt_b = 0,0
    for j in i:
        for k in i:
            if j ==k:continue
            cnt_a += arr[j-1][k-1]
    for j in team_b:
        for k in team_b:
            if j==k:continue
            cnt_b += arr[j-1][k-1]
    ans = min(ans,abs(cnt_a-cnt_b))
    if ans == 0:
        break
print(ans)
