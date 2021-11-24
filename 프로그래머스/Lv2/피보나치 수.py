def solution(n):
    answer = 0
    arr = [0,1]
    for i in range(2,n+1):
        arr.append(arr[i-2]+arr[i-1])
    answer = arr[n]%1234567
    # print(answer)
    return answer
solution(3)
solution(5)