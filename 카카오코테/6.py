def solution(board, skill):
    answer = 0
    def skills(s,r1,c1,r2,c2,degree):
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                if s == 1:
                    board[r][c] -= degree
                else:
                    board[r][c] += degree
    for i in skill:
        skills(i[0],i[1],i[2],i[3],i[4],i[5])

    for r in board:
        for c in r:
            if c >0 :
                answer += 1

    return answer
solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])