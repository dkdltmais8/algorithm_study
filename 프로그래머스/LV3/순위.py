def solution(n, results):
    def store(lst,idx):
        win =[]
        lose = []
        for i,v in enumerate(lst):
            if v == 1:
                win.append(i)
            elif v == -1:
                lose.append(i)
        for i in win:
            change(player[i],lose)
        for i in lose:
            changewin(player[i],win)
    def change(lst,lose):
        for i in lose:
            lst[i] = -1
    def changewin(lst,win):
        for i in win:
            lst[i] = 1
    answer = 0
    player = [[0 for i in range(n)] for _ in range(n)]
    for i in results:
        player[i[0]-1][i[1]-1] = 1
        player[i[1]-1][i[0]-1] = -1
    for idx,j in enumerate(player):
        # if 1 in j and -1 in j:
        store(j,idx)
    # print(player)
    for i in player:
        cnt = 0
        for j in i:
            if j==1 or j==-1:
                cnt +=1
        if cnt ==n-1:
            answer+=1
    # print(answer)
    return answer
solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])