def solution(n, m):
    answer = []
    if n > m:
        n,m = m,n
    big = 0
    small = 0
    for i in range(1,n+1):
        if n%i == 0 and m% i == 0:
            big=i
    small=(m*n)//big
    answer.append(big)
    answer.append(small)
    # print(answer)
    return answer

def solution(n, m):
    answer = []
    if n > m:
        n,m = m,n
    big = 0
    small =0
    def gcd(a,b):
        nonlocal big
        if b%a == 0:
            big = a
        else:
            gcd(b%a,a)
    gcd(n,m)
    small = (n*m)//big
    answer.append(big)
    answer.append(small)
    # print(answer)
    return answer
solution(3,12)
solution(2,5)
