from collections import Counter
n = int(input())
ans = 0
for _ in range(n):
    flag = True
    p = input()
    ex = Counter(p)
    for i in ex:
        if ex[i] == 1:
            continue
        else:
            cnt = ex[i]
            now = p.index(i)
            for j in range(now,now+cnt):
                if p[j] != i:
                    flag = False
                    break
    if flag:
        ans += 1
print(ans)