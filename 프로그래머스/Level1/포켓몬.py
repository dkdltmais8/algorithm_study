def solution(nums):
    answer = 0
    lst = []
    nums.sort()
    n = len(nums)//2
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1] and len(lst)< n:
            lst.append(nums[i])
    if nums[-1] not in lst and len(lst) < n:
        lst.append(nums[-1])
    answer = len(lst)
    print(lst)
    return answer
solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])