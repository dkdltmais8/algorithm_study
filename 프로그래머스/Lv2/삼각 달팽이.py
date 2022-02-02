def solution(n):
    answer = [[0]*i for i in range(1,n+1)]
    d = -1
    idx = 0
    cnt = 1
    for i in range(n):
        for j in range(i,n):
            #내려갈때
            if i%3 == 0:
                d+=1
            #수평 이동할 때
            elif i%3 == 1:
                idx += 1
            #올라갈 때
            else:
                idx-=1
                d-=1
            answer[d][idx] = cnt
            cnt += 1
    answer = sum(answer,[])
    return answer
solution(4)

