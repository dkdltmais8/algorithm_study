def solution(d, budget):
    answer = 0
    d.sort()
    print(d)
    tot = budget
    for i in range(len(d)):
        tot -= d[i]
        answer += 1
        if tot < 0:
            tot +=d[i]
            answer -= 1
            break
    print(tot)
    print(answer)
    return answer
solution([1,3,2,5,4],9)