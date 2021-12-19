from collections import defaultdict
n = int(input())
arr = list()
dic = dict()
dic = defaultdict(int)
for _ in range(n):
    arr.append(input())
arr.sort(key=lambda x: -len(x))
for i in arr:
    for j in range(len(i)):
        dic[i[j]] += 10**(len(i)-j-1)
# print(dic)
dic = sorted(dic.values(),reverse=True)
# print(dic)
tot = 0
num = 9
for i in dic:
    tot += i*num
    num-=1
print(tot)