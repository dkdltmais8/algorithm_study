whole = input()
ex = input()
now = 0
cnt = 0
while now < len(whole):
    if whole[now:].find(ex) != -1:
        now += len(ex)+whole[now:].find(ex)
        cnt += 1
    else:
        break
print(cnt)