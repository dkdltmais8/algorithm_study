for tc in range(1, 11):
    li = []
    total = 0
    total_sero_li = []
    total_garo_li = []
    total_daegak_li = []
    N = int(input())
    for i in range(100):
        ans = list(map(int, input().split()))
        li.append(ans)

    for y in range(100):
        for x in range(100):
            total += li[x][y]
        total_sero_li.append(total)
        total = 0

    for x in range(100):
        for y in range(100):
            total += li[x][y]
        total_garo_li.append(total)
        total = 0

    for x in range(100):
        total += li[x][x]
        total_daegak_li.append(total)
        total = 0
    if max(total_garo_li) >= max(total_sero_li) and max(total_garo_li) >= max(total_daegak_li):
        print(f"#{tc} {max(total_garo_li)}")
    elif max(total_sero_li) >= max(total_garo_li) and max(total_sero_li) >= max(total_daegak_li):
        print(f"#{tc} {max(total_sero_li)}")
    elif max(total_daegak_li) >= max(total_sero_li) and max(total_daegak_li) >= max(total_garo_li):
        print(f"#{tc} {max(total_daegak_li)}")