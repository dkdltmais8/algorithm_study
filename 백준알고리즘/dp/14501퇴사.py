n = int(input())
table = [list(map(int,input().split())) for i in range(n)]
arr = []
for i in range(len(table)):
    arr.append(table[i][1])
arr.append(0)

for i in range(n-1,-1,-1):
    #일 끝나는 시간이 퇴사 후인 경우 = 페이를 추가할 수 없는 경우
    if table[i][0] + i >n:
        arr[i] = arr[i+1]
    else:
        arr[i] = max(arr[i+1],table[i][1]+arr[i+table[i][0]])
print(arr[0])