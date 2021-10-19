def solution(s):
    answer = True
    ans=''
    for i in s:
        ans += i.lower()
    cnt_p = ans.count('p')
    cnt_y = ans.count('y')
    print(cnt_p,cnt_y)
    if cnt_y != cnt_p:
        answer = False
    print(ans)
    return answer
solution('pPoooyY')