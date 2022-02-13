from collections import deque
from copy import deepcopy
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def solution(game_board, table):
    def bfs(idx):
        lst = [[idx[0],idx[1]]]
        Q = deque()
        visit[idx[0]][idx[1]] = 1
        Q.append(idx)
        while Q:
            r,c = Q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<len(game_board) and 0<= nc < len(game_board[0]) and table[nr][nc] == 1:
                    if visit[nr][nc] == 0:
                        visit[nr][nc] = 1
                        Q.append((nr,nc))
                        lst.append([nr,nc])
        candidate.append(sorted(change(lst)))
    def bfs2(idx):
        lst2 = [[idx[0],idx[1]]]
        Q = deque()
        visit[idx[0]][idx[1]] = 1
        Q.append(idx)
        while Q:
            r,c = Q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<len(game_board) and 0<= nc < len(game_board[0]) and game_board[nr][nc] == 0:
                    if visit[nr][nc] == 0:
                        visit[nr][nc] = 1
                        Q.append((nr,nc))
                        lst2.append([nr,nc])
        candidate2.append(sorted(change(lst2)))
    def lotate(lst):
        r = len(lst)
        res = []
        for i in lst:
            res.append([i[1],r-1-i[0]])
        return sorted(change(res))
    def change(lst):
        minr = sorted(lst,key=lambda x:x[0])[0][0]
        minc = sorted(lst,key=lambda x:x[1])[0][1]
        for i in range(len(lst)):
            lst[i][0] = lst[i][0]-minr
            lst[i][1] = lst[i][1]-minc
        return lst

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

    for i in candidate2:
        for j in candidate:
            if len(i)!=len(j):
                continue
            else:
                if i == j:
                    answer += len(j)
                    candidate.remove(j)
                    break
                else:
                    a = deepcopy(j)
                    flag = False
                    for _ in range(4):
                        a = lotate(a)
                        if i == a:
                            answer += len(j)
                            candidate.remove(j)
                            flag = True
                            break
                    if flag:
                        break
    # print(answer)
    return answer
solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])