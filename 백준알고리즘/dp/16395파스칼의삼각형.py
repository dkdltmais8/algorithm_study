n, k = map(int,input().split())
arr = [[i for _ in range(i)] for i in range(1,31)]
arr[1] = [1,1]
for i in range(2,30):
    arr[i][0],arr[i][-1] = 1,1
    for j in range(1,i):
        arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
print(arr[n-1][k-1])








