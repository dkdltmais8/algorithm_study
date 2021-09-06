T = int(input())
for tc in range(1, T+1):
    num, cnt = map(int, input().split())
    num = str(num)
    for i in range(cnt):
        for j in range(len(num)-1):
            if num[j] < num[j+1]:
                
