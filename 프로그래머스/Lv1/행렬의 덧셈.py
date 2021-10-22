def solution(arr1, arr2):
    answer = [[]]
    d = len(arr1)
    dd = len(arr1[0])
    for i in range(d):
        for j in range(dd):
            arr2[i][j] += arr1[i][j]
    answer = arr2
    return answer