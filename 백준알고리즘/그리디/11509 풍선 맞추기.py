n = int(input())
lst = list(map(int,input().split()))
cnt = 0
visit = [0]*1000001
for i in range(n):
    if visit[lst[i]] == 0:
        cnt += 1
        visit[lst[i]-1] += 1
    else:
        visit[lst[i]] -= 1
        visit[lst[i]-1]+=1
print(cnt)