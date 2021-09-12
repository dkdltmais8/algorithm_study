def solution(n, k):
    answer = -1
    def decimal_to(n,k):
        global ans
        if n == 0:
            return ans
        if k == 10:
            return str(n)[::-1]
        ans += str(n%k)
        n = n//k
        return decimal_to(n,k)
    def prime(num):
        global tot
        if num == 1 or num ==[]:
            return 0
        d = num//2
        for i in range(2,d+1):
            if num % d == 0:
                return 0
        else:
            tot += 1
            return
    decimal_to(n,k)
    res = ''
    res = ans[::-1]
    # print(res)
    candidate = ['' for _ in range(1000)]
    cnt = 0
    string= ''
    for i in res:
        if i == '0':
            cnt += 1
            candidate[cnt]=(string)
            string = ''
        else:
            string += i
    if string != '':
        candidate.append(string)
    # print(candidate)
    for i in candidate:
        if i != '':
            prime(int(i))
    print(tot)
    return answer
ans=''
tot =0
solution(437674	,3)