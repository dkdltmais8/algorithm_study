def solution(n, money):
    rest = [1] + [0] * n
    for m in money:
        for i in range(m, n+1):
            rest[i] += rest[i-m]
    return rest[n] % 1000000007
solution(5,[1,2,5])