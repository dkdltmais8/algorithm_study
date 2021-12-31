from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def back():
    visit = [[0,0,0,0,0] for _ in range(5)]
    for i in candi:
        visit[i//5][i%5] = 1
    Q = deque()
    Q.append(candi[0])
    depth = 0
    visit[candi[0]//5][candi[0]%5] = 0
    while Q:
        depth += 1
        idx = Q.popleft()
        for i in range(4):
            nr = idx//5+dr[i]
            nc = idx%5+dc[i]
            if 0<=nr<5 and 0<=nc<5 and visit[nr][nc] == 1:
                visit[nr][nc] = 0
                Q.append(nr*5+nc)
    if depth == 7:
        return 1
    else:
        return 0
def dfs(depth,idx,cnt_y,cnt_s):
    global ans
    if depth == 7 and cnt_s>=4:
        if back():
            ans += 1
        return
    if cnt_y >= 4 or idx>=25 or depth>7:
        return
    r = idx // 5
    c = idx % 5
    candi.append(idx)
    if arr[r][c] == 'Y':
        dfs(depth+1,idx+1,cnt_y+1,cnt_s)
    elif arr[r][c] == 'S':
        dfs(depth+1,idx+1,cnt_y,cnt_s+1)
    candi.pop()
    dfs(depth,idx+1,cnt_y,cnt_s)

arr = list(input() for _ in range(5))
candi = []
ans = 0
dfs(0,0,0,0)
print(ans)
