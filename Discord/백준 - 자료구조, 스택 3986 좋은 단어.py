
ans = 0
for _ in range(int(input())):
    lst = []
    p = input()
    if p.count('A')%2 or p.count('B')%2:
        continue
    for i in p:
        if not lst:
            lst.append(i)
            continue
        if i == lst[-1]:
            lst.pop()
        else :
           lst.append(i)
    if not lst:
        ans += 1
print(ans)