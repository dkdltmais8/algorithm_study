arr = input()
cnt = 0
ans = []
for i in arr:
    if i =='X':
        cnt += 1
        continue
    if i =='.' and cnt!= 0:
        ans.append(cnt)
        ans.append('')
        cnt = 0
        continue
    if i =='.' and cnt == 0:
        ans.append('')
        continue
if cnt != 0:
    ans.append(cnt)
answer = ""
for i in ans:
    if i=='':
        answer += '.'
        continue
    while i>1:
        if i >=4:
            answer+="AAAA"
            i-=4
            continue
        if i>=2:
            answer+="BB"
            i-=2
            continue
    if i<0 or i%2:
        answer = -1
        break
print(answer)
