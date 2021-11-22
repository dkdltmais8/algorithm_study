def solution(s):
    def check(s,tot):
        nonlocal cnt, answer
        ans = ""
        for i in s:
            if i != "0":
                ans += i
            else:
                cnt += 1
        d = len(ans)
        if d == 1:
            answer.append(tot)
            answer.append(cnt)
            return
        else:
            s = bin(d)[2:]
            # print(s)
            check(s,tot+1)
    answer = []
    cnt = 0
    check(s,1)
    # print(answer)
    return answer

solution("110010101001")
