m,n = map(int,input().split())
arr = [[[[0 for _ in range(2)] for _ in range(2)] for _ in range(m)] for _ in range(n)]
for i in range(1,n):
    arr[i][0][0][1] = 1
for i in range(1,m):
    arr[0][i][1][1] = 1
for i in range(1,n):
    for j in range(1,m):
        #x축 이동에 회전 불가능은 바로 직전에 한번 회전한 것 -> y축이동이고 회전가능한 놈
        arr[i][j][0][0] = arr[i-1][j][1][1]
        #x축 이동에 회전 가능인 것은 직전에 x축 이동이거나 전전에 y축이동에서 회전한놈 ->회전 여부와 상관없이 직전에 x축이동
        arr[i][j][0][1] = arr[i-1][j][0][0] + arr[i-1][j][0][1]
        #y축 이동에 회전 불가능 -> 직전에 x축 이동이였고 회전가능했던 놈
        arr[i][j][1][0] = arr[i][j-1][0][1]
        #y축이동이고 회전 가능 -> 직전에 y축이동이였던 모든놈들
        arr[i][j][1][1] = arr[i][j-1][1][0] + arr[i][j-1][1][1]
ans = sum(arr[n-1][m-1][0])+sum(arr[n-1][m-1][1])
print(ans%100000)