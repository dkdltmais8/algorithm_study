import itertools
def dfs(idx):
    global ans,win,lose,same
    if idx == 15:
        if win.count(0) == 6 and lose.count(0) == 6 and same.count(0)==6:
            ans = 1
        return
    p1,p2 = arr2[idx]
    if win[p1] > 0 and lose[p2] > 0:
        win[p1] -= 1
        lose[p2] -= 1
        dfs(idx+1)
        win[p1] += 1
        lose[p2] += 1
    if win[p2] > 0 and lose[p1] > 0:
        win[p2] -= 1
        lose[p1] -= 1
        dfs(idx+1)
        win[p2] += 1
        lose[p1] += 1
    if same[p1] > 0 and same[p2] > 0:
        same[p1] -= 1
        same[p2] -= 1
        dfs(idx+1)
        same[p1] += 1
        same[p2] += 1

arr1 = [list(map(int,input().split())) for _ in range(4)]
arr2 = list(itertools.combinations(range(6),2))
for i in range(4):
    ans = 0
    win,lose,same = [],[],[]
    for j in range(18):
        if j % 3 == 0:
            win.append(arr1[i][j])
        elif j % 3 == 1:
            same.append(arr1[i][j])
        elif j % 3 == 2:
            lose.append(arr1[i][j])
    dfs(0)
    print(ans,end=' ')

