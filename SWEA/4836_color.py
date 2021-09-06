T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    purple = [[0]*10 for _ in range(10)]
    for i in range(N):
        x1, x2, y1, y2, color = map(int, input().split())
        for row in range(x1,y1+1):
            for column in range(x2,y2+1):
                purple[row][column] += color
    for row in range(10):
        for column in range(10):
            if purple[row][column] == 3:
                cnt += 1

    print(f"#{tc} {cnt}")