def solution(left, right):
    answer = 0
    def medicine(num):
        d = num // 2
        ans = []
        for i in range(2, d+1):
            if num % i == 0:
                ans.append(i)
                # print(i)
        return num if len(ans) % 2 ==0 else (num*-1)
    for i in range(left,right+1):
        answer+=medicine(i)
    print(answer)
    return answer
solution(13	,17)
solution(24,27)