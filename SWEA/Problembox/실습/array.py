T = int(input())
for tc in range(1, T+1):
    n = int(input())
    board = list(map(int,input().split()))
    ans = 1000000000000
    for i in range(1,n-1):
        for j in range(i,n):
            a = sum(board[:i])
            b = sum(board[i:j])
            c = sum(board[j:])
            diff = abs(max(a,b,c) - min(a,b,c))
            if diff < ans :
                ans = diff
    print("#{} {}".format(tc, ans))
