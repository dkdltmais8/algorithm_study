T = int(input())
for tc in range(1, T+1):
    w = int(input())
    num = [list(map(int,input().split())) for _ in range(w)]
    ans = []
    for r in range(w):
        for c in range(w):
            for i in range(1,w):
                if r-i >= 0 and c-i >=0:






    print(max(ans))
