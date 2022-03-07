def check(n):
    lst = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            lst.extend([i,n//i])
    lst = list(set(lst))
    lst.remove(1)
    return lst
n = int(input())
arr = list(map(int,input().split()))
x = int(input())
a = check(x)
print(a)
tot,cnt = 0,0
for i in arr:
    if i == x:
        continue
    for j in a:
        if i%j == 0:
            break
    else:
        tot += i
        cnt += 1
print(tot/cnt)
