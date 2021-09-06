T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    point = n // 2
    tot = 0
    r, c = point, 0
    while  n > c >= 0:

        if c <= point:

            for i in range(point-c, point+c+1):
                tot += farm[i][c]
            c += 1
        elif c > point:

            for i in range(c - point, n - c + point):
                tot += farm[i][c]
            c += 1
    print("#{} {}".format(tc,tot))