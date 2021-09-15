def solution(n):
    answer = 0
    def de_tri(num):
        ans = ''
        while num > 0:
            ans += str(num % 3)
            num  //= 3
        return ans
    def tri_de(num):
        ans = 0
        cnt = 1
        for i in range(len(num)-1,-1,-1):
            ans += int(num[i])*cnt
            cnt *= 3
        return ans
    answer = de_tri(n)
    answer = tri_de(answer)
    print(answer)
    return answer
solution(45)