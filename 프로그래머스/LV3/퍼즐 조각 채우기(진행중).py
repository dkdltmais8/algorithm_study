from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def solution(game_board, table):
    def bfs(idx):
        lst = [(0,0)]
        Q = deque()
        visit[idx[0]][idx[1]] = 1
        Q.append(idx)
        x,y = idx[0],idx[1]
        while Q:
            r,c = Q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<len(game_board) and 0<= nc < len(game_board[0]) and table[nr][nc] == 1:
                    if visit[nr][nc] == 0:
                        visit[nr][nc] = 1
                        Q.append((nr,nc))
                        lst.append((nr-x,nc-y))
        candidate.append(lst)
    def bfs2(idx):
        lst2 = [(0,0)]
        Q = deque()
        visit[idx[0]][idx[1]] = 1
        Q.append(idx)
        x,y = idx[0],idx[1]
        while Q:
            r,c = Q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<len(game_board) and 0<= nc < len(game_board[0]) and game_board[nr][nc] == 0:
                    if visit[nr][nc] == 0:
                        visit[nr][nc] = 1
                        Q.append((nr,nc))
                        lst2.append((nr-x,nc-y))
        candidate2.append(lst2)
    def lotate(lst):
        r = len(lst)
        res = [[0]*r for _ in range(r)]
        for i in range(r):
            for j in range(r):
                res[j][r-i-1] = lst[i][j]
        return sorted(res)
    answer = 0
    candidate = []
    candidate2 = []
    visit = [[0]*len(game_board[0]) for _ in range(len(game_board))]
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if table[i][j] == 1 and visit[i][j] == 0:
                bfs((i,j))
    visit = [[0]*len(game_board[0]) for _ in range(len(game_board))]
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if game_board[i][j] == 0 and visit[i][j] == 0:
                bfs2((i,j))
    print(candidate)
    print(candidate2)
    for i in candidate2:
        for j in candidate:
            if len(i)!=len(j):
                continue
            else:
                flag = False
                if i == j:
                    answer += len(j)
                    candidate2.remove(j)
                else:
                    for a in j:

                    for _ in range(3):
                        j = lotate(j)
                        if i == j:
                            answer += len(j)
                            candidate2.remove(j)
                            flag = True
                            break
                    if flag:
                        break


    return answer
solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])