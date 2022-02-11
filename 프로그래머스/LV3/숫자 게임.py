import heapq
def solution(A, B):
    answer = 0
    heapq.heapify(A)
    heapq.heapify(B)
    for i in range(len(A)):
        a = heapq.heappop(A)
        b = heapq.heappop(B)
        if a<b:
            answer += 1
        else:
            heapq.heappush(A,a)
        # print(a,b,A,B)
    return answer
solution([5,1,3,7],[2,2,6,8])