from collections import defaultdict
p = list(map(str,input()))
p.sort()
dic = defaultdict(int)
m = ''
ans = ""
for i in p:
    dic[i] += 1
cnt = 0
for i,v in dic.items():
    if cnt>=2:
        break
    if v%2:
        cnt += 1
        m+=i
        p.remove(i)
for i in range(0,len(p),2):
    ans+=p[i]
if cnt>=2:
    print("I'm Sorry Hansoo")
else:
    print(ans+m+ans[::-1])

