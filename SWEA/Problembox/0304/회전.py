from collections import deque
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    board = deque(map(int,input().split()))
    for i in range(m):
        board.append(board.popleft())
    print("#{} {}".format(tc,board[0]))
