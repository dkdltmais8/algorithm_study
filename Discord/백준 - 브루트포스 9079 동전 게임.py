from collections import deque

def col_change(idx):
    for i in range(3):
        arr[i][idx] = abs(int(arr[i][idx])-1)
def row_change(idx):
    for i in range(3):
        arr[idx][i] = abs(int(arr[idx][i])-1)
def cross_change(idx):
    for i in range(3):
        if idx == 0:
            arr[i][i] = abs(int(arr[i][i])-1)
        else:
            arr[i][2-i] = abs(int(arr[i][2-i])-1)
def correct():
    a = arr[0][0]
    for i in range(3):
        for j in range(3):
            if arr[i][j] != a:
                return False
    return True
def makeint():
    now = 0
    for i in range(3):
        for j in range(3):
            now = now*2+arr[i][j]
    return now
def makestr(num):
    global arr
    for i in range(2,-1,-1):
        for j in range(2,-1,-1):
            arr[i][j] = num%2
            num//=2

n = int(input())
for _ in range(n):
    visit = [0] * 512
    arr = [list(map(str,input().split())) for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 'H':
                arr[i][j] = 1
            else:
                arr[i][j] = 0
    now = makeint()
    Q = deque([[now,0]])
    visit[now] = 1
    flag = True
    while Q:
        now,cnt = Q.popleft()
        makestr(now)
        if correct():
            print(cnt)
            flag = False
            break
        for i in range(3):
            col_change(i)
            next = makeint()
            if not visit[next]:
                visit[next] = 1
                Q.append([next,cnt+1])
            col_change(i)
        for i in range(3):
            row_change(i)
            next = makeint()
            if not visit[next]:
                visit[next] = 1
                Q.append([next, cnt + 1])
            row_change(i)
        for i in range(3):
            cross_change(i)
            next = makeint()
            if not visit[next]:
                visit[next] = 1
                Q.append([next, cnt + 1])
            cross_change(i)
    if flag:
        print(-1)



