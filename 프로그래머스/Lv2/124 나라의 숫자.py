def solution(n):
    def cal(n):
        answer = ''
        while n > 0:
            if str(n%3) == '0':
                answer += '4'
                n = n//3-1
            else:
                answer += str(n%3)
                n //= 3
        return answer
    answer = cal(n)
    answer = answer[::-1]
    print(n,answer)
    return answer
solution(1)
solution(2)
solution(3)
solution(4)
solution(5)
solution(6)
solution(7)
solution(8)
solution(9)
solution(10)
