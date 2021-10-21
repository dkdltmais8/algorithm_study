def solution(arr):
    answer = []
    i = arr.index(min(arr))
    arr.pop(i)
    if len(arr)>0:
        answer = arr
    else:
        answer = [-1]
    return answer
solution([4,3,2,1])