def solution(n, left, right):
    answer = []
    idx1 = (left//n)+1
    idx2 = (right//n)+1
    now = left
    while now <right+1:
        i = (now//n)+1
        if now%n<i:
            answer.append(i)
        else:
            answer.append(now%n+1)
        now += 1
    # print(answer)
    return answer

solution(3,2,5)
solution(4,7,14)