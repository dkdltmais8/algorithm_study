def find_cloud():
    global candidate
    for r in range(n):
        for c in range(m):
            if arr[r][c] =='c':
                candidate.append((r,c))
                res[r][c] = 0

n,m = map(int,input().split())
arr = [input() for _ in range(n)]
res =[[-1 for _ in range(m)]for i in range(n)]
candidate = []
find_cloud()
for i in range(len(candidate)):
    r,c = candidate[i][0],candidate[i][1]
    cnt = 0
    while c < m-1:
        c += 1
        if arr[r][c] =='c':
            break
        cnt += 1
        res[r][c] = cnt
for i in res:
    print(*i)

