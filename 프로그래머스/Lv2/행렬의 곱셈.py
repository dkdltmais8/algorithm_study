def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    # 232   543
    # 424   241
    # 314   311
    # 14    33
    # 32    33
    # 41
    # 123     14
    # 456     25
    #         36
    def cal(lst,idx):
        tot = 0
        for c in range(len(arr2[0])):
            for i in range(len(lst)):
                # for r in range(len(arr2)):
                tot += lst[i]*arr2[i][c]

            answer[idx].append(tot)
            tot = 0
    for i in range(len(arr1)):
        cal(arr1[i],i)
    print(answer)
    return answer
solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]])
solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],	[[5, 4, 3], [2, 4, 1], [3, 1, 1]])
solution([[1, 2, 3], [4, 5, 6]],[[1, 4], [2, 5], [3, 6]])