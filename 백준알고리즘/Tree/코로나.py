import sys
from collections import deque

input = sys.stdin.readline
for tc in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())

    city = [list(map(int, input().split())) for _ in range(n)]

    que = deque()
    que.append((0, 0, k, 0))

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    ans = -1
    while que:

        r, c, cnt, bit = que.popleft()
        if r == n - 1 and c == m - 1:
            ans = max(ans, cnt)
            continue

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                b = nr * m + nc
                if bit & (1 << b) == 0:
                    if city[nr][nc]:
                        que.append((nr, nc, cnt + city[nr][nc] - 1, bit | (1 << b)))
                    else:
                        que.append((nr, nc, cnt - 1, bit | (1 << b)))

    print(f'#{tc} {ans}')