def solution(weights, head2head):
    answer = []
    n = len(weights)
    res = [[0,0,0,0] for _ in range(n)]
    win_rate = [[0,0] for _ in range(n)]
    super_win =[[0,0] for _ in range(n)]
    for i in range(len(head2head)):
        cnt = 0
        real_cnt = 0
        for j in range(len(head2head[i])):
            if head2head[i][j] == 'W':
                if weights[i] < weights[j]:
                    super_win[i][0] += 1
                cnt += 1
                super_win[i][1] = i+1
            elif head2head[i][j] =='N':
                real_cnt += 1
        if real_cnt != n:
            win_rate[i][0] = cnt/(n-real_cnt)
        else:
            win_rate[i][0] = 0
        win_rate[i][1] = i+1
    for i in range(n):
        res[i][0] = win_rate[i][0]
        res[i][1] = super_win[i][0]
        res[i][2] = weights[i]
        res[i][3] = i+1
    # print(res)

    res = sorted(res,key = lambda x:(x[0],x[1],x[2],-x[3]),reverse=True)
    for i in res:
        answer.append(i[3])
    # print(answer)
    return answer
solution([50,82,75,120],	["NLWL","WNLL","LWNW","WWLN"])
solution([145,92,86],	["NLW","WNL","LWN"])
solution([60,70,60]	,["NNN","NNN","NNN"])

# 리스트에 고려해야 할 데이터를 다 넣어주고 sorted, key, lamba를 이용해 한 번에 정렬해 준다.
# lambda 안에 여러 개의 원소를 적용할 수 있다는 것을 알게 되었다.