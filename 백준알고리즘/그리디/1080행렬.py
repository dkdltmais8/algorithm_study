def change(r,c):
    for i in range(r,r+3):
        for j in range(c,c+3):
            A[i][j] = 1-A[i][j]
n,m = map(int,input().split())
A = []
B = []
cnt = 0
for i in range(n):
    A.append(list(map(int, input())))
for i in range(n):
    B.append(list(map(int, input())))
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            change(i,j)
            cnt += 1

if A==B:
    print(cnt)
else:
    print(-1)
