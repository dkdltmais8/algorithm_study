T = int(input())
for i in range(T):
    L, U, X = map(int, input().split())
    if L <= X <= U:
        print(f"#{i + 1} 0")
    elif U <= X:
        print(f"#{i + 1} -1")
    elif X < L:
        print(f"#{i+1} {L - X}")