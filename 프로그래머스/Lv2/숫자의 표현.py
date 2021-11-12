def solution(n):
    def check(num):
        nonlocal answer
        ans = 0
        for i in range(num,n+1):
            ans += i
            if ans == n:
                answer += 1
                return
            if ans>n:
                return

    answer = 0
    lst = [i for i in range(1,n+1)]
    for i in lst:
        check(i)
    print(answer)
    return answer
solution(15)

# 처음에는 그냥 자연수인줄 알고 부분집합을 어떻게 가질지 막막했는데
# 자세히 읽어보니 "연속된" 자연수였다..