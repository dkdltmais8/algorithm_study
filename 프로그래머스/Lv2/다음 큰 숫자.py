def solution(n):
    answer = 0
    cnt = 0
    j = bin(n)
    for k in j:
        if k == '1':
            cnt += 1
    for i in range(n+1,n+10):
        j = bin(i)
        if j.count('1') == cnt:
            answer = i
            break


    print(answer)
    return answer
solution(78)
solution(15)