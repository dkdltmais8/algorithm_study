def solution(num):
    answer = -1
    cnt = 0
    while cnt<= 500 or num > 1:
        if num == 1:
            break
        if num%2:

            num = ((num*3)+1)
            cnt += 1
        else:
            num = (num//2)
            cnt += 1
    if cnt <500:
        answer = cnt
    return answer