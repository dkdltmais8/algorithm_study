T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    s = 0
    for r in range(N):
        for c in range(N):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    s += arr[nr][nc]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
    print(f"#{tc} {r} {c} {s}")