n = int(input())
answer= 0
for i in range(1,n):
    tot = i
    a= str(i)
    for j in a:
        tot += int(j)
    if tot ==  n:
        answer = i
        break
print(answer)