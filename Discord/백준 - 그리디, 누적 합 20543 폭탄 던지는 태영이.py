import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = [[0]*n for _ in range(n)]
if m == 1:
    for i in arr:
        for j in i:
            print(-j,end=' ')
        print()
else:
    for i in range(n):
        for j in range(n):
            r = i+m//2 if i+m//2<n else n-1
            c = j+m//2 if j+m//2<n else n-1
            rr = i-m//2-1 if i-m//2-1>=0 else 0
            cc = j-m//2-1 if j-m//2-1>=0 else 0
            if r>=n or c>=n: continue
            ans[r][c] = ans[r-1][c] + ans[r][c-1] - ans[r-1][c-1]
            next = -1*((ans[r][c]-ans[r][cc]-ans[rr][c]+ans[rr][cc]) + arr[i][j])
            ans[r][c] += next
    for i in range(n):
        for j in range(n):
            r = i-1 if i-1>=0 else 0
            c = j-1 if j-1>=0 else 0
            next = ans[i][j]-ans[r][j]-ans[i][c]+ans[r][c]
            print(next,end = ' ')
        print()
