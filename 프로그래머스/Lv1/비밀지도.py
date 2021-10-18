def solution(n, arr1, arr2):
    answer = ['' for _ in range(n)]
    board1 = ['' for _ in range(n)]
    board2 = ['' for _ in range(n)]
    for i in range(n):
        board1[i]=bin(arr1[i])[2:].zfill(n)
    for i in range(n):
        board2[i]=bin(arr2[i])[2:].zfill(n)
    for i in range(n):
        for j in range(n):
            if board1[i][j] =='1' or board2[i][j] =='1':
                answer[i] += '#'
            else:
                answer[i] += ' '
    # print(answer)
    return answer
solution(5,[9,20,28,18,11],[30,1,21,17,28])