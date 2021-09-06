for tc in range(1, 11):
    L = int(input())
    cal = list(map(int,input().split('+')))
    print(f"#{tc} {sum(cal)}")