# n,m = map(str,input().split())
# floor = [input() for _ in range(n)]
# cnt = 0
# for r in range(n):
#     j=0
#     while j < m:


n, m = map(int, input().split())
floor = [input() for _ in range(n)]
cnt = 0
for r in range(n):
    c = 0
    while c < m:
        if floor[r][c] == '|':
            c += 1
        else:
            cnt += 1
            while c < m and floor[r][c] == '-':
                c += 1
for c in range(m):
    r = 0
    while r < n:
        if floor[r][c] == '-':
            r += 1
        else:
            cnt += 1
            while r < n and floor[r][c] == '|':
                r += 1
print(cnt)