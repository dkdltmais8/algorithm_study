def multiple(a, b):
    if b > 1:
        b -= 1
        a = A * a
        return multiple(a, b)
    elif b == 1:
        return a


for i in range(10):
    N = int(input())
    A, B = map(int, input().split())
    print(f"#{N} {multiple(A, B)}")
