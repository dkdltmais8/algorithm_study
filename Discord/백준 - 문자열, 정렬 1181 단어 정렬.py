from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
dic = defaultdict(set)
for i in range(n):
    a = input().rstrip('\n')
    dic[len(a)].add(a)
lst = sorted(dic.keys())
for i in lst:
    for j in sorted(dic[i]):
        print(j)