import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)