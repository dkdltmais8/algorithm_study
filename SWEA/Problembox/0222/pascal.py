T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ans = [[1]*n for _ in range(n)]
    for r in range(2,n):
        for c in range(1,r):
            ans[r][c] = ans[r-1][c-1] + ans[r-1][c]
    print("#{}".format(tc))
    for i in range(n):
        for j in range(i+1):
            print(ans[i][j], end=' ')
        print()
