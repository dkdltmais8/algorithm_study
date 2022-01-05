n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer = []
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            tot = arr[i]+arr[j]+arr[k]
            answer.append((abs(tot-m),tot))
            if tot >= m:
                break
answer.sort()
for i in answer:
    if i[1]<=m:
        print(i[1])
        break
