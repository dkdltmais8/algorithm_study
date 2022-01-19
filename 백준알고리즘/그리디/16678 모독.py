n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
tot = 0
s = 1
for i in range(n):
    d = arr[i]-s
    if d>=0:
        tot += d
        s+= 1
print(tot)