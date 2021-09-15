def solution(numbers, hand):
    answer = ''
    board = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    L = [(3,0)]
    R = [(3,2)]
    for i in numbers:
        for r in range(4):
            for c in range(1):
                if i == board[r][c]:
                    answer += 'L'
                    L.append((r,c))
        for r in range(4):
            for c in range(2,3):
                if i == board[r][c]:
                    answer += 'R'
                    R.append((r,c))
        for r in range(4):
            for c in range(1,2):
                if i == board[r][c]:
                    L_x, L_y = L.pop()
                    R_x, R_y = R.pop()
                    if abs(L_x-r)+abs(L_y-c) > abs(R_x-r)+abs(R_y-c):
                        answer += 'R'
                        R.append((r,c))
                        L.append((L_x,L_y))
                    elif abs(L_x-r)+abs(L_y-c) < abs(R_x-r)+abs(R_y-c):
                        answer +='L'
                        L.append((r,c))
                        R.append((R_x,R_y))
                    else:
                        if hand == 'right':
                            answer += 'R'
                            R.append((r, c))
                            L.append((L_x,L_y))
                        else:
                            answer += 'L'
                            L.append((r, c))
                            R.append((R_x, R_y))
        print(L,R,answer)

    return answer
