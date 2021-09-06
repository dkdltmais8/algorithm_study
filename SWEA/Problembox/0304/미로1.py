dr = [0,-1,0,1]
dc = [-1,0,1,0]

def start():
    for r in range(16):
        for c in range(16):
            if miro[r][c] == '2':
                return r,c

def findroad(start_point):
    global ans
    r, c = start_point[0], start_point[1]
    if miro[r][c] == '3':
        ans = 1
        return ans
    visited.append((r,c))
    for i in range(4):
        nr, nc = r+dr[i],c + dc[i]
        if 0 <= nr < 16 and 0 <= nc < 16 and (nr,nc) not in visited and (miro[nr][nc] == '0' or miro[nr][nc] == '3'):
            findroad((nr,nc))



for tc in range(1,11):
    n = int(input())
    miro = [list(input()) for _ in range(16)]
    visited = []
    ans = 0
    findroad(start())

    if ans == 0:
        print("#{} 0".format(tc))
    else:
        print("#{} 1".format(tc))


