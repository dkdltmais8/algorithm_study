from itertools import combinations
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
arr = [i for i in range(n)]
team = []
for i in list(combinations(arr,n//2)):
    team.append(i)
min_gap = 1000000
for i in range(len(team)//2):
    A = team[i]
    point_A=0
    for j in range(n//2):
        p = A[j]
        for k in A:
            point_A += board[p][k]
    B = team[-i-1]
    point_B = 0
    for j in range(n // 2):
        p = B[j]
        for k in B:
            point_B += board[p][k]
    min_gap = min(min_gap,abs(point_B-point_A))
print(min_gap)