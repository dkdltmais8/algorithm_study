import heapq
def solution(operations):
    answer = []
    q = []
    for i in operations:
        i = i.split(' ')
        if i[0] == "I":
            heapq.heappush(q,int(i[1]))
        else:
            if len(q) == 0:
                continue
            if i[1][0] == '-':
                heapq.heappop(q)
            else:
                q.pop()
    if len(q) == 0:
        answer = [0,0]
    else:
        answer.append(max(q))
        answer.append(min(q))
    # print(answer)
    return answer
solution(["I 16","D 1"])
solution(["I 7","I 5","I -5","D -1"])