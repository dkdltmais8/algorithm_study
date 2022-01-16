n,m = map(int,input().split())
arr = list(map(int,input().split()))
minus = []
plus = []
tot = []
for i in arr:
    if i<0:
        minus.append(i)
    else:
        plus.append(i)
minus.sort()
plus.sort(reverse=True)
for i in range(len(minus)//m):
    tot.append(abs(minus[i*m]))
if len(minus)%m>0:
    tot.append(abs(minus[(len(minus)//m)*m]))
for i in range(len(plus)//m):
    tot.append(plus[i*m])
if len(plus)%m>0:
    tot.append(plus[(len(plus)//m)*m])
tot.sort()
ans = sum(tot)*2
ans -= tot[-1]
print(ans)