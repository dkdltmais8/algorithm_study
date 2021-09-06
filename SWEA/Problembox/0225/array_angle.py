T = int(input())
for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    arr = []
    arr1 = []
    arr2 = []
    arr3 = []
    for r in range(n):
        for c in range(n-1,-1,-1):
            arr.append(board[c][r])
        arr1.append(arr)
        arr = []
    for r in range(n):
        for c in range(n-1,-1,-1):
            arr.append(arr1[c][r])
        arr2.append(arr)
        arr = []
    for r in range(n):
        for c in range(n-1,-1,-1):
            arr.append(arr2[c][r])
        arr3.append(arr)
        arr = []
    print("#{}".format(tc))
    for r in range(n):
        for c in range(n-1):
            print(arr1[r][c],end= '')
        for c in range(n-1,n):
            print(arr1[r][c], end = ' ')
        for c in range(n-1):
            print(arr2[r][c],end='')
        for c in range(n-1,n):
            print(arr2[r][c], end= ' ')
        for c in range(n):
            print(arr3[r][c], end= '')

        print()
