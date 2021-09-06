def dfs(idx):
    global cnt
    if idx == 10:
        point = 0
        for j in range(10):
            if arr[j] == board[j]:
                point += 1
        if point >= 5:
            cnt += 1
        return
    for i in range(1,6):
        if idx > 1 and arr[idx-2] == arr[idx-1] == i:
            continue
        arr.append(i)
        dfs(idx+1)
        arr.pop()
board = list(map(int,input().split()))
arr = []
cnt = 0
dfs(0)
print(cnt)
