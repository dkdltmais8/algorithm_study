def check(arr):
    global ans,n
    #좌표를 돌면서 하나씩 확인
    while arr:
        r,c = arr.pop()
        #팔방탐색을 통해 만약 0이 있다면 그 자리는 지뢰가 없는 것이기 때문에 멈춘다.
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if (nr == 0 or nr == n-1) or (nc == 0 or nc == n-1):
                if board[nr][nc] == 0:
                    break
        #멈추는 조건에 걸리지 않은 경우 지뢰가 무조건 있는 것이기 때문에 팔방탐색을 해서 테두리인 부분을 다 1씩 감소
        else:
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if (nr == 0 or nr == n-1) or (nc == 0 or nc == n-1):
                    board[nr][nc] -= 1
            #지뢰를 하나 발견했으니까 ans 1증가
            ans += 1
    return
dr = [-1,0,1,-1,1,-1,0,1]
dc = [-1,-1,-1,0,0,1,1,1]
n = int(input())
board = [list(map(str,input())) for _ in range(n)]
lst = []
ans = 0
#테두리만 알 수 있기 떄문에 최대치를 구하기 위해서 가운데는 전부 지뢰가 있다고 가정
if n>=5:
    ans += (n-4)**2
#맵을 돌면서 테두리와 인접한 공간에서 #인 곳을 리스트에 채워주고 #이 아닌 것을 int로 변환
for r in range(n):
    for c in range(n):
        if r == 1 or r == n-2:
            if board[r][c] == '#':
                lst.append((r,c))
            else:
                board[r][c] = int(board[r][c])
        elif 1<r<n-2:
            if c == 1 or c == n-2:
                lst.append((r,c))
            else:
                if board[r][c] != "#":
                    board[r][c] = int(board[r][c])
        else:
            if board[r][c] != '#':
                board[r][c] = int(board[r][c])
check(lst)
print(ans)