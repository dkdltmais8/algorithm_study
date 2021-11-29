from itertools import permutations
def solution(numbers):
    def check(n):
        if n == 1 or n==0:
            return False
        for i in range(2,(n//2)+1):
            if n%i == 0:
                return False
        return True
    answer = 0
    numbers = list(numbers)
    ans = []
    res = []
    for i in range(1,len(numbers)+1):
        res.append(list(permutations(numbers,r=i)))
    # print(res)
    for i in res:
        for j in i:
            ans.append(''.join(j))
    # print(ans)
    for i in range(len(ans)):
        ans[i] = int(ans[i])
    ans = list(set(ans))
    # print(ans)
    for i in ans:
        if check(int(i)):
            answer += 1
    # print(answer)
    return answer
solution("17")
solution("011")