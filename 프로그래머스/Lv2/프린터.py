from collections import deque

def solution(priorities, location):
    arr = []
    for i in range(len(priorities)):
        arr.append([priorities[i],i])
    arr = deque(arr)
    cnt = 0
    #print(arr)
    while True:
        res = arr.popleft()
        if len(arr)>=1:
            for data in arr:
                if res[0] < data[0]:
                    arr.append(res)
                    break
            if res != arr[-1]:
                cnt += 1
                # print(arr)
                # print(res)
                # print(cnt)
                if res[1] == location:
                    break
        else:
            cnt+=1
            break
    return cnt
solution([2, 1, 3, 2]	,2)
solution([1, 1, 9, 1, 1, 1]	,0)