from itertools import permutations
def solution(numbers):
    answer = 0
    res = list(permutations(numbers))
    numbers = list(numbers)
    numbers.sort(reverse=True)
    ans = ''
    for i in numbers:
        ans+= i
    ans = int(ans)
    lst = [1]*(ans+1)
    m = int(ans**0.5)
    for i in range(2,m+1):
        if lst[i] == 1:
            for j in range(i+i,ans+1,i):
                lst[j] = 0
    lst[0],lst[1] = 0,0
    print(res)
    print(lst)
    for i,v in enumerate(lst):
        if v == 1 and str(i) in res:
            answer += 1
    print(answer)
    return answer
solution("17")