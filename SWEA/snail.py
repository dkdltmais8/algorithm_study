delta = ((0,1), (1,0), (0,-1), (-1,0), )
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ans = [[0] * n for _ in range(n)]
    r, c = 0, 0
    start = 1
    move = max(n-1, 1)
    while True:
        for i in range(4):
            for _ in range(move):
                ans[r][c] = start
                start += 1

                dr, dc = delta[i]
                r += dr
                c += dc
                if start > n**2:
                    break
    print('#%d' % tc)
    for row in range(n):
        for col in range(n):
            print(ans[row][col], end=' ')
        print()












