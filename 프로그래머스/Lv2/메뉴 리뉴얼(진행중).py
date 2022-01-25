from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course:
        can = []
        for j in orders:
            can += combinations(sorted(j),i)
        cnt = Counter(can)
        if len(cnt) != 0 and max(cnt.values())>=2:
            answer += [''.join(k) for k in cnt if cnt[k] == max(cnt.values())]

    return sorted(answer)
solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])