from collections import Counter
for _ in range(int(input())):
    s = input()
    k = int(input())
    Q = Counter(s)
    can = []
    ans1,ans2 = float('inf'),0
    for i in Q.items():
        if i[1]>=k:
            can.append(i[0])
    if not can:
        print(-1)
        continue
    for i in can:
        a = s.split(i)
        for j in a[1:-1]:
            ans1 = min(ans1,len(j)+k)
            ans2 = max(ans2,len(j)+k)
    print(ans1,ans2)