n, m = map(int, input().split())
scores = {}
for i in range(n):
    a = list(map(int,input().split()))
    scores[a[0]] = a[1:]
cnt = 1
for i in range(1, n+1):
    if scores[m][0] < scores[i][0]:
        cnt += 1
    elif scores[m][0] == scores[i][0]:
        if scores[m][1] < scores[i][1]:
            cnt +=1
        elif scores[m][1] == scores[i][1]:
            if scores[m][2] < scores[i][2]:
                cnt +=1
print(cnt)