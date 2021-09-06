for tc in range(1,11):
    a = int(input())
    num = list(map(int, input().split()))
    while num[7] > 0:
        for i in range(5):
            num[0] = num[0]-(i+1)
            if  num[0] < 0:
                num[0] = 0
            num[0],num[1],num[2],num[3],num[4],num[5],num[6],num[7] = num[1],num[2],num[3],num[4],num[5],num[6],num[7],num[0]

    print(f"#{a} {' '.join(map(str, num))}")
