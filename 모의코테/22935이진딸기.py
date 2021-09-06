for tc in range(int(input())):
    num = int(input())  1~15  30~43  58~71
    a = 0                16~29 44~57
    if 0 < num < 16:
        num = num
    elif 15 < num < 30:
        num = 30 - num
    elif 29 < num < 44:
        num = num - 28
    else:
        a = num // 28
        num = num%28


    ans = list(bin(num))
    ans = ans[2:]
    if len(ans) < 4:
        ans = ans[::-1]
        while len(ans) < 4:
            ans.append('0')
            if len(ans) == 4:
                ans = ans[::-1]
                break
    res=""
    for z in ans:
        if z == "1":
            res += "딸기"
        else:
            res += "V"
    print(res)