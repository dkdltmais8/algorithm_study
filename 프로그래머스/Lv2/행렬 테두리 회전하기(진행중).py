def solution(rows, columns, queries):
    def rotate(lst):
        nonlocal answer,arr
        sr,sc = lst[0]-1,lst[1]-1
        er,ec = lst[2]-1,lst[3]-1
        tmp = arr[sr][sc]
        mini = tmp
        for r in range(sr,er):
            move = arr[r+1][sc]
            arr[r][sc] = move
            mini = min(mini,move)
        for c in range(sc,ec):
            move = arr[er][c+1]
            arr[er][c] = move
            mini = min(mini,move)
        for r in range(er,sr,-1):
            move = arr[r-1][ec]
            arr[r][ec] = move
            mini = min(mini,move)
        for c in range(ec,sc,-1):
            move = arr[sr][c-1]
            arr[sr][c] = move
            mini = min(mini,move)
        arr[sr][sc+1] = tmp
        answer.append(mini)
    answer = []
    arr =[[0]*columns for _ in range(rows)]
    t = 1
    for r in range(rows):
        for c in range(columns):
            arr[r][c] = t
            t += 1
    for i in queries:
        rotate(i)
    return answer
# solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])
solution(3,	3	,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])