def solution(N, number):
    answer = -1
    ans = [{}]+[{int(str(N)*i)} for i in range(1,9)]
    for i in range(1,9):
        for j in range(1,i):
            for n in ans[j]:
                for m in ans[i-j]:
                    ans[i].add(n+m)
                    ans[i].add(n-m)
                    ans[i].add(n*m)
                    if m != 0:
                        ans[i].add(n//m)
        if number in ans[i]:
            answer = i
            break
    return answer
solution(5,12)
# solution(2,11)
# 1.나눌 수 있을때까지 나누고 나머지는 1로 더해주기
# 2.1,11,111등으로 나누고 나머지를 더해주기
# 3.분자를 다 더해서 한번에 나눠주기