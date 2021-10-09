n = int(input())
m = int(input())
s = input()
ans,cnt = 0, 0
i = 1
while i < m-1:
    if s[i - 1] == 'I' and s[i] == 'O' and s[i + 1] == 'I':
        cnt += 1
        i += 2
        if cnt == n:
            ans += 1
            #연속적으로 중첩되기 위해서 1번만 줄여준다.
            cnt -= 1
    else:
        i += 1
        cnt = 0
print(ans)
