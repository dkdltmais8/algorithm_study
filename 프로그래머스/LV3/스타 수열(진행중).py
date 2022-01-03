from collections import defaultdict
def solution(a):
    answer = 0
    if len(a)<=1:
        return 0
    cnt = defaultdict(int)
    for i in a:
        cnt[i] += 1
    cnt = sorted(cnt.items(),key=lambda x:-x[1])
    for n in cnt:

        if n[1] *2 <= answer:
            continue
        idx = 1
        ans = 0
        while idx<len(a):
            if (a[idx] == a[idx-1]) or (n[0] != a[idx] and n[0] != a[idx-1]):
                idx +=1
                continue
            ans += 2
            idx += 2
        answer = max(ans,answer)
    return answer
solution([0])
solution([5,2,3,3,5,3])