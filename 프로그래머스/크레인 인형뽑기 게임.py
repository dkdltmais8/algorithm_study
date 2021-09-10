def solution(board, moves):
    answer = 0
    store = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if store == []:
                    store.append(board[j][i - 1])
                    board[j][i - 1] = 0
                    break
                if store[-1] == board[j][i-1]:
                    board[j][i-1] = 0
                    answer+=2
                    store.pop()
                    break
                store.append(board[j][i-1])
                board[j][i-1] = 0
                break
    # print(answer,store)
    return answer
solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])