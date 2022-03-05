def check(p):
    global cnt
    for i in p:
        i = i.split("'")
        if len(i)== 1:
            cnt += 1
        else:
            if i[0] in ['c', 'j', 'n', 'm', 't', 's', 'l', 'd', 'qu', 's'] and i[1][0] in ('a','e','i','o','u','h'):
                cnt += 2
            else:
                cnt+=1

p = input().split(' ')
cnt = 0
for i in range(len(p)):
    p[i] = p[i].split('-')
    check(p[i])
print(cnt)