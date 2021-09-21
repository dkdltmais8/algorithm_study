
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break
        answer += 1
        scoville.append(scoville.pop(0)+scoville.pop(0)*2)
        scoville.sort()
    return answer

#힙큐 쓰기
def solution(scoville, K):
    import heapq
    count = 0
    heapq.heapify(scoville)
    if scoville[0] >= K:
        return count
    while len(scoville) >= 2:
        count += 1
        temp = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, temp)
        if scoville[0] >= K:
            return count
    if scoville[0] < K:
        return -1

solution([1, 2, 3, 9, 10, 12],7)
solution([7,7,7,7,7,7,7],7)
solution([1,1,1],100)