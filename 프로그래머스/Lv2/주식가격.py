def solution(prices):
    d = len(prices)
    answer = [0]*d
    for i in range(d):
        for j in range(i,d):
            if i==j:
                continue
            if prices[i] <= prices[j]:
                answer[i]+= 1
            else:
                answer[i]+=1
                break
    print(answer)
    return answer
solution([1, 2, 3, 2, 3])