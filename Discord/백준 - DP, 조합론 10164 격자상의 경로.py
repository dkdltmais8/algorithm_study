def check(idx):
    n,m = idx
    arr = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i ==0 or j == 0:
                arr[i][j] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            arr[i][j] = arr[i][j-1]+arr[i-1][j]
    return arr[-1][-1]
n,m,k = map(int,input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
cnt = 1
now = []
for i in range(n):
    for j in range(m):
        arr[i][j] = cnt
        if cnt == k:
            now.append((i,j))
        cnt += 1
if k == 0:
    print(check((n-1,m-1)))
else:
    print(check((now[0][0],now[0][1]))*check((n-now[0][0]-1,m-now[0][1]-1)))
# print(arr)