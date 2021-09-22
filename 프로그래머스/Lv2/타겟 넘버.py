def solution(numbers, target):
    answer = 0
    def dfs(num,depth):
        nonlocal answer
        if depth == len(numbers):
            if num == target:
                answer += 1
            return
        lst = [num, -num]
        if depth == 1:
            for i in range(2):
                dfs(lst[i] + numbers[depth],depth + 1)
                dfs(lst[i] - numbers[depth], depth + 1)
        else:
            dfs(num + numbers[depth], depth + 1)
            dfs(num - numbers[depth], depth + 1)
    dfs(numbers[0],1)
    return answer
solution([1, 1, 1, 1, 1],3)