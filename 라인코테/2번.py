def solution(research, n, k):
    answer = ''
    for i in research:
        for j in i:
            if j not in answer:
                answer += j
    ans= [[] for _ in range(len(research))]
    for i in answer:
        new_cnt = 0
        for r in range(len(research)):
            lst = research[r:r+n]
            cnt = 0
            tot = 0
            for c in lst:
                tot += c.count(i)
                if c.count(i) >= k:
                    cnt += 1
                # print(tot, cnt)
                if cnt == n and 2*n*k <= tot:
                    new_cnt += 1
                if new_cnt >= 1:
                    ans[new_cnt].append(i)
    for i in range(1,len(ans)):
        ans[i] = list(set(ans[i]))
        ans[i].sort()
    print(max(ans))


solution(["abaaaa","aaa","abaaaaaa","fzfffffffa"],2,2)
