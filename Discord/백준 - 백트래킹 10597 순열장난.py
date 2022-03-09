def dfs(idx,v):
    global flag,answer
    if flag: return
    if idx == len(n):
        if v == max_num:
            flag = True
            answer = " ".join(map(str,ans))
        return
    num = int(n[idx])
    #1의 자리 숫자부터 채우고
    if not visit[num]:
        visit[num] = 1
        ans[v] = num
        dfs(idx+1,v+1)
        visit[num] = 0
    if idx < len(n)-1:
        num = int(n[idx:idx+2])
        if num <= max_num and not visit[num]:
            visit[num] = 1
            ans[v] = num
            dfs(idx+2,v+1)
            visit[num] = 0
n = input()
answer = ""
if len(n)<10:
    max_num = len(n)
else:
    max_num = 9+(len(n)-9)//2
visit = [0] * (max_num+1)
ans = [0]*(max_num)
flag = False
dfs(0,0)
print(answer)
