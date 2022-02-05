def solution(n, t, m, p):
    def change(num):
        s = ''
        if num == 0:
            s = '0'
        while num>0:
            nam = num%n
            if nam == 10:
                nam = 'A'
            elif nam == 11:
                nam = 'B'
            elif nam == 12:
                nam= 'C'
            elif nam == 13:
                nam = 'D'
            elif nam == 14:
                nam = 'E'
            elif nam == 15:
                nam = 'F'
            else:
                nam = str(nam)
            s += str(nam)
            num //= n
        s = s[::-1]
        return s
    answer = ''
    d = t*m
    for i in range(d):
        answer += change(i)
    res = ''
    for i in range(p-1,d,m):
        res += answer[i]
    return res
solution(2,4,2,1)
# solution(16,16,2,1)
# solution(16,16,2,2)