n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(key= lambda x:(x%10,x//10))
cnt = 0
i = 0
#한번 짤랐을 때 나머지가 없으면 1번 잘라서 2개 만들고
#나머지가 있으면 2번 잘라야 2개 만들 수 있음
while i<=n-1:
    if arr[i]<10:
        i+=1
        continue
    if arr[i]== 10:
        cnt += 1
        i += 1
        continue
    if arr[i]>10:
        if arr[i]%10 ==0:
            if m>=((arr[i]//10)-1):
                m -= ((arr[i]//10)-1)
                cnt += arr[i]//10
                i += 1
            else:
                cnt += m
                m = 0

        else:
            if m>=((arr[i]//10)):
                m -= ((arr[i]//10))
                cnt += arr[i]//10
                i += 1
            else:
                cnt += m
                m = 0

    if m ==0:
        break
print(cnt)
