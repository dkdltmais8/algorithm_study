n = int(input())
p = ""
for i in range(n):
    p+=input()
ans = ""
s,e = 0,n-1
while s<=e:
    if p[s]<p[e]:
        ans+=p[s]
        s += 1
    elif p[s]>p[e]:
        ans += p[e]
        e -= 1
    else:
        ns,ne = s,e
        flag = False
        #비교값이 같은 경우에는 새로운 투 포인터를 만들어 그 안에서 비교를 하고 더 작은 게 있는 쪽을 먼저 없앤다.
        while ns<=ne:
            if p[ns]<p[ne]:
                ans += p[s]
                s += 1
                flag = True
                break
            elif p[ns]>p[ne]:
                ans += p[e]
                e -= 1
                flag = True
                break
            else:
                ns += 1
                ne -= 1
        if not flag:
            ans += p[s]
            s += 1
    if len(ans)%80-ans.count('\n') == 0:
        ans += '\n'
print(ans)