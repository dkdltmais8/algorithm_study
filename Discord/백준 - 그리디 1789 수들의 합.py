n = int(input())
i = 1
tot = 0
while 1:
    tot += i
    if tot>n:
        break
    i+=1
print(i-1)