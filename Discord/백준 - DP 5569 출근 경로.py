m,n = map(int,input().split())
arr = [[[[0 for _ in range(2)] for _ in range(2)] for _ in range(m)] for _ in range(n)]
for i in range(1,n):
    arr[i][0][0][1] = 1
for i in range(1,m):
    arr[0][i][1][1] = 1
for i in range(1,n):
    for j in range(1,m):
        arr[i][j][0][0] = arr[i-1][j][1][1]
        arr[i][j][0][1] = arr[i-1][j][0][0] + arr[i-1][j][0][1]
        arr[i][j][1][0] = arr[i][j-1][0][1]
        arr[i][j][1][1] = arr[i][j-1][1][0] + arr[i][j-1][1][1]
ans = sum(arr[n-1][m-1][0])+sum(arr[n-1][m-1][1])
print(ans%100000)