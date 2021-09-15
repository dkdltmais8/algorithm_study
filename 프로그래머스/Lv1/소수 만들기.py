import itertools
def solution(nums):
    answer = 0
    ans = list(itertools.combinations(nums,3))
    for i in ans:
        d = sum(i)//2
        for j in range(2,d+1):
            if sum(i) % j == 0:
                break
        else:
            answer += 1
    return answer
solution([1,2,7,6,4])