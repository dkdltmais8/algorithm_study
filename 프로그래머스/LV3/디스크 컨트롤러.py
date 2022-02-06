import heapq
def solution(jobs):
    answer = 0
    q = []
    end = 0
    cnt = 0
    start = -1
    while cnt<len(jobs):
        for i in jobs:
            if start < i[0]<=end:
                heapq.heappush(q,[i[1],i[0]])
        if len(q)>0:
            n = heapq.heappop(q)
            start = end
            end += n[0]
            answer += (end-n[1])
            cnt += 1
        else:
            end += 1
    return answer//len(jobs)
solution([[0, 3], [1, 9], [2, 6]])
solution([[0, 5], [2, 10], [10000, 2]])