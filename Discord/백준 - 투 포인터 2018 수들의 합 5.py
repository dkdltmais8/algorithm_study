n = int(input())
s,e = 0,1
cnt = 0
tot = 1
while s<=n and s<=e:
    if tot<n:
        e += 1
        tot += e
    elif tot == n:
        cnt+=1
        e+=1
        tot -= s
        tot += e
        s+=1
    else:
        tot-=s
        s+=1
print(cnt)