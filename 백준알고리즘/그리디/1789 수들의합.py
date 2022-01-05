s = int(input())
cnt = 0
tot = 0
for i in range(1,s+1):
    tot += i
    cnt += 1
    if tot == s:
        print(cnt)
        break
    elif tot > s:
        print(cnt-1)
        break
