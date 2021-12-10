def solution(s):
    answer = 0
    d = len(s)
    ans = []
    for i in range(d-2):
        if s[i] == s[i+1]:
            st,e = i,i+1
            while st>=0 and e<=d-1 and s[st]==s[e]:
                answer = max(answer,e-st+1)
                st -= 1
                e += 1
        if s[i] == s[i+2]:
            st, e = i, i + 2
            while st >= 0 and e <= d - 1 and s[st]==s[e]:
                answer = max(answer, e - st + 1)
                st -= 1
                e += 1
    # print(answer)
    return answer
solution("abacde")