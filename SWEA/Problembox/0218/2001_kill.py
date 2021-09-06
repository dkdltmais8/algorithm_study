T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    ans = []
    for r in range(n-m+1):
        for c in range(n-m+1):
            total = 0
            for i in range(m):
                for j in range(m):
                    total += board[r+i][c+j]
            ans.append(total)
    print("#{} {}".format(tc,max(ans)))
