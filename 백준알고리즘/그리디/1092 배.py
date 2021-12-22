n = int(input())
arr1 = list(map(int,input().split()))
arr1.sort(reverse=True)

m = int(input())
arr2 = list(map(int,input().split()))
arr2.sort(reverse=True)

time = 0
count = 0
#박스 방문체크
visit = [0]*m
#현재 상태
position = [0]*n
if arr1[0] < arr2[0]:
    time = -1
else:
    while count<len(arr2):
        time += 1
        for i in range(n):
            # print(position, time, visit,'1')
            while position[i] < len(arr2):
                if not visit[position[i]] and arr1[i]>=arr2[position[i]]:
                    visit[position[i]] = 1
                    position[i] += 1
                    count += 1
                    break
                position[i] += 1
                # print(position,time,visit)
print(time)

