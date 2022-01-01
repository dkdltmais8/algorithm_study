import heapq
def solution(n, works):
    answer = 0
    pq = []
    for i in works:
        heapq.heappush(pq,(-i,i))

    for _ in range(n):
        m1,m2 = heapq.heappop(pq)
        if m1 == 0:
            break
        m1 +=1
        m2 -= 1
        heapq.heappush(pq,(m1,m2))
    for i in pq:
        answer += i[1]**2
    # print(answer)
    return answer
solution(4,[4,3,3])