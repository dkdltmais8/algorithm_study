from collections import defaultdict
n = int(input())
list = [input() for _ in range(n)]
cnt = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        s1 = list[i]
        s2 = list[j]
        flag = True
        visit1 = defaultdict(str)
        visit2 = defaultdict(str)
        for k in range(len(s1)):
            idx1 = s1[k]
            idx2 = s2[k]

            if idx1 not in visit1 and idx2 not in visit2:
                visit1[idx1] = s2[k]
                visit2[idx2] = s1[k]
            elif visit1[idx1] != s2[k]:
                flag = False
                break
        if flag:
            cnt += 1
print(cnt)