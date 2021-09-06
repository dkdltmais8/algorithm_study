import sys
put = int(input())
for i in range(put):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    print(a + b)
