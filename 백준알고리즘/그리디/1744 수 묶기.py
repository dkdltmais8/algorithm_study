n = int(input())
plus = []
zero = []
minus = []
tot = []
for i in range(n):
    a = int(input())
    if a> 0:
        plus.append(a)
    elif a == 0:
        zero.append(a)
    else:
        minus.append(a)
flagp = False
flagM = False
plus.sort(reverse=True)
minus.sort()
if n == 1:
    if minus:
        tot.append(minus[0])
    if zero:
        tot.append(0)
    if plus:
        tot.append(plus[0])
else:
    for i in range(len(plus)):
        if i == len(plus)-1 and not flagp:
            tot.append(plus[i])
            break
        if flagp:
            flagp = False
            continue
        if plus[i+1]>1:
            tot.append(plus[i]*plus[i+1])
            flagp = True
        else:
            tot.append(plus[i])

    for i in range(len(minus)):
        if i == len(minus)-1 and not flagM:
            if zero:
                tot.append(0)
                zero.pop()
            else:
                tot.append(minus[i])
            break
        if flagM:
            flagM = False
            continue
        if minus[i+1]<=-1:
            tot.append(minus[i]*minus[i+1])
            flagM = True
print(sum(tot))
