n = int(input())
p = '666'
idx = 666
cnt = 0
while 1:
    if p in str(idx):
        cnt += 1
    if cnt == n:
        break
    idx += 1
print(idx)