from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def solution(places):
    answer = []
    def check(lst):
        res = []
        ans1 = []
        ans2 = []
        for r in range(5):
            for c in range(5):
                if lst[r][c] == 'P':
                    ans1.append((r,c))
                if lst[r][c] == 'O':
                    ans2.append((r,c))
        for i in ans1:
            res.append(bfs(i[0],i[1],lst))
        for i in ans2:
            res.append(bfs2(i[0],i[1],lst))
        if 0 in res:
            return 0
        else:
            return 1
    def bfs(r,c,lst):
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<5 and 0<=nc<5:
                if lst[nr][nc] == 'P':
                    return 0
        return 1
    def bfs2(r,c,lst):
        cnt = 0
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<5 and 0<=nc<5:
                if lst[nr][nc] == 'P':
                    cnt += 1
        if cnt<2:
            return 1
        else:
            return 0

    for i in places:
        answer.append(check(i))
    print(answer)
    return answer
solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])