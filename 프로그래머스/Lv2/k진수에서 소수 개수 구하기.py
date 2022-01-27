def change(n,k):
    ans = ""
    while n>0:
        ans += str(n%k)
        n//=k
    ans = ans[::-1]
    return ans
def check(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    else:
        return True
def solution(n, k):
    answer = 0
    ex = change(n,k)
    ex = ex.split('0')
    for i in ex:
        if i == "":
            continue
        if check(int(i)):
            answer += 1
    return answer
solution(437674	,3)
solution(110011	,10)
solution(7,2)