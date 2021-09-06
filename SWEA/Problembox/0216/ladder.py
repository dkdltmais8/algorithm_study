def end(arr):
    for i in range(len(arr)):
        if arr[99][i] == 2:
            return i
def road(arr,goal):
    r = 99
    c = goal
    dir = 'U'
    while r > 0:
        if dir == 'U':
            if 0 <= c - 1 <100 and arr[r][c-1] == 1:
                c -= 1
                dir = 'L'
            elif 0 <= c + 1 < 100 and arr[r][c+1] == 1:
                c += 1
                dir = 'R'
            else:
                r -= 1
        elif dir == 'L':
            if arr[r-1][c] == 1:
                r -= 1
                dir = 'U'
            else:
                c -= 1
        else:
            if arr[r-1][c] == 1:
                r -= 1
                dir ='U'
            else:
                c += 1
    return c

for tc in range(1, 11):
    n = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    ans = end(ladder)
    result = road(ladder,ans)
    print('#{} {}' .format(tc, result))