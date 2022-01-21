n = int(input())
lst = []
tot = 0
for i in range(n):
    info = list(map(int, input().split()))
    tot += info[1]
    lst.append(info)
lst.sort(key=lambda x:x[0])
m = tot//2
if tot%2:
    m += 1
num = 0
for i in lst:
   num+= i[1]
   if num>=m:
       print(i[0])
       break
