# idx
for tc in range(1,11):
    a = int(input())
    num = list(map(int, input().split()))
    while num[7] > 0:
        for i in range(5):
            num[0] = num[0]-(i+1)
            if num[0] < 0:
                num[0] = 0
            num[0],num[1],num[2],num[3],num[4],num[5],num[6],num[7] = num[1],num[2],num[3],num[4],num[5],num[6],num[7],num[0]
            if num[7] == 0:
                break
    ans = ' '.join(map(str,num))
    print("#{} {}".format(tc, ans))


# deque
from collections import deque

for tc in range(1, 11):
    n = input()
    string = deque(map(int,input().split()))
    start = 1
    while True:
        back = string.popleft()
        if back - start <= 0:
            string.append(0)
            break
        else:
            string.append(back-start)
        start += 1
        if start > 5:
            start = 1
    print("#" + str(tc), *string)