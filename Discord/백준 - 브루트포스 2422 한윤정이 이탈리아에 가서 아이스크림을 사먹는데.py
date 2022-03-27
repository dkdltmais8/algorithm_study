from itertools import combinations
n,m = map(int,input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1
answer = 0
for i in combinations(range(n),3):
    if arr[i[0]][i[1]] or arr[i[0]][i[2]] or arr[i[1]][i[2]]:
        continue
    else:
        answer += 1
print(answer)