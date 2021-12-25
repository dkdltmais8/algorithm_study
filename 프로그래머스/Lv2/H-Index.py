def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    for i in range(n-1,-1,-1):
        h = i+1
        cnt_use = 0
        cnt_notuse = 0
        for j in citations:
            if j<=h:
                cnt_notuse+=1
            if j>=h:
                cnt_use += 1
        if cnt_use>=h and cnt_notuse<=h:
            answer = h
            break
    #
    # print(citations)
    # print(answer)
    return answer
solution([3,0,6,1,5])