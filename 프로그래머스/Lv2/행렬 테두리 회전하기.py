def solution(rows, columns, queries):
    answer = []
    arr = [list(0 for _ in range(columns)) for i in range(rows)]
    tot = 1
    for r in range(rows):
        for c in range(columns):
            arr[r][c] = tot
            tot += 1
    for i in queries:
        tmp = []
        start = arr[i[0]-1][i[3]-1]
        for c in range(i[3]-1,i[1]-1,-1):
            arr[i[0]-1][c] = arr[i[0]-1][c-1]
            tmp.append(arr[i[0]-1][c])
        for r in range(i[0] - 1, i[2] - 1):
            arr[r][i[1] - 1] = arr[r + 1][i[1] - 1]
            tmp.append(arr[r][i[1] - 1])
        for c in range(i[1]-1)
    print(arr)
    return answer
solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])