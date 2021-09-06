n = int(input())
cnt = 0
while n > 0:
    if n > 3:
        n -= 3
        cnt += 1
    else:
        n -= 1
        cnt += 1
if cnt % 2 == 0:
    print('CY')
else:
    print('SK')